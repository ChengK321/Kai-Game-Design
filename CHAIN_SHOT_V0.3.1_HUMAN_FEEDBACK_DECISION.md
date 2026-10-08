# Chain Shot V0.3.1 — Human Audio / Visual Feedback Decision

> Recorded: 2026-10-09
> Source: user's first-hand subjective A/B feedback after trying V0.3.1
> Scope: presentation direction and next experimental gate; **no code or level changes**
> Evidence status: **internal playtest (n=1)**, not external retention or a controlled multi-user study

## What the human actually reported (OBSERVED)

- Original synthesized **Hit** is more comfortable than the real-sample options tested.
- **Classic** is clearer and more comfortable than Balloon Blast.
- Lukeo135 Pop sounds like a **machine gun** during chains.
- Breviceps Pop is quite crisp, but repetitive and monotonous.
- The tester wonders whether a real explosion sound would improve if paired with better explosion visuals. This is a **hypothesis**, not a preference result or an approved request to implement a new animation.

No real device/headphone configuration, exact paired trial counts or external player sample size were reported. Do not invent them.

## Code-backed observations (FACT from current `prototype/chain-shot-v0.3.1.html`)

1. `flushImpacts()` in synth mode executes `sound('hit', n.depth)` **for each activated node**. `sound()` derives a depth-dependent musical note from a small scale. It is not a static identical sound on every activation.
2. Pop mode plays **one audio buffer per simulation tick group**, with 4 cycling playback rates `[1, .99, 1.015, .985]` and small group-size gain changes, regardless of number of activated nodes in the batch. Its repeated timbre and relatively fixed timing could create monotonous or machine-gun perception.
3. Blast renders activated nodes as faint outlined circles plus original-arrow ghosts (global alpha .25 for the outline); Classic retains a more prominent activated-node glyph. Both modes use the same gameplay simulation.
4. The earlier report documented 1,100 seed/mode comparisons versus the Solver and no reported console errors. **Those are prior archived test claims, not freshly executed checks in this decision.**

## Causal interpretations: still unproven

- **INFERENCE:** The synth mode's depth-linked tonal progression and the Pop mode's repeated, grouped buffer playback partly explain why one feels more satisfying.
- **INFERENCE:** A persistent illuminated arrow better communicates the chain's history and post-failure information than fading it into a weak ghost.
- **HYPOTHESIS:** 'Node activation' and 'physical destruction' may be mismatched event semantics for this version of the game.
- **ALTERNATIVE HYPOTHESIS:** The Pop audiovisual mismatch or insufficient animation could explain part of the negative result. We have **not** cleanly isolated that explanation.
- **IMPORTANT:** Improved animation might still improve a different, intentionally destructive mechanic; this does not justify another FX build now.

## Decision

**KEEP**: Classic + synthesized Hit as the current playable champion/baseline.

**HOLD / NOT SELECTED**: Lukeo135 Pop, Breviceps Pop, and Balloon Blast for the default experience. Retain FX Lab and alternatives for reproducibility; do not delete them or imply they failed a public player trial.

**DO NOT BUILD YET**: new explosion visual systems, more samples, layered audio middleware, extra content or new core rules.

**NEXT GATE**: shift attention from an FX optimization loop to **puzzle-depth and voluntary retry**. The V0.3 playtest review already flags that all 10 levels have a unique zero-in-degree winning Seed, and L5/L7 often leave only 1–2 unactivated nodes after a wrong Seed. This is a structural risk; further sound polish cannot prove or repair it.

## One cheapest next experiment — no code needed

Ask **3–5 people who have not studied the game** to play Classic + synthesized Hit (existing V0.3.1), beginning with a clear starter board and including L5 and L7 if feasible. Avoid revealing Solver/Seed hints. Keep an observer log for each player:

- What they think tapping will do *before* the first tap
- Whether they deliberately inspect arrows, or tap at random
- Initial Seed and stated or inferred reason (do not prompt an answer beforehand)
- After a wrong attempt, whether the next Seed is chosen for a reason
- Whether the remaining nodes make the answer trivially obvious; compare L5/L7 observations
- Whether they **voluntarily retry** and request another level, versus merely replaying an effect
- One unsolicited phrase describing the moment they found most interesting

Keep game instructions identical among participants. Report counts and direct quotes with test conditions, not a guessed retention percentage.

**Decision readout:** If causal prediction and voluntary retry appear, invest next in level-quality tuning within the existing One-Rule system; if responses are primarily random tapping, instant post-failure deduction or 'watched once, done', return to `kai-mechanic-gate` before further polish.

## Skill evaluation note

`kai-game-feel` is useful here to separate feedback layers and resist implementing an unsupported animation hypothesis; `kai-game-qa` distinguishes correctness/archived browser assertions from subjective enjoyment. **No controlled Skill-vs-no-Skill paired run or new runtime execution has occurred**, so there is no measured evidence yet of productivity gain. Keep both Skills in experimental status.

## Decision log

- **Decision**: freeze FX candidate selection; keep Classic+synth and investigate puzzle depth next.
- **Supporting evidence**: one firsthand player report; current source code; archived deterministic QA report.
- **Counter-evidence**: alternate Pop/Blast assets may perform better with different synchronization or semantics; n=1.
- **Unknowns**: external player behavior, repeat motivation, affect under a precisely matched audio-visual comparison.
- **Kill / revise condition**: repeated new-player trials show no thoughtful seed selection, no reasoned retries, and no voluntary repeat despite comprehensible feedback.
- **Next evidence**: small blinded-to-Solver observational playtest using unchanged Classic+synth, L5/L7 included.
