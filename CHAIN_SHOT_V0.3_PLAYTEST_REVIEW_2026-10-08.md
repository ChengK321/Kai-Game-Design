# Chain Shot V0.3 Playtest Review — 2026-10-08

> Status: REVIEW / no code change, no V0.4 approval
> Source: user-played V0.3 feedback; current pushed code at commit `edddcb7f03baaac8d4c4a4fcd9f623305424e646`
> Scope: Sound / Impact / Blast readability / post-failure information gain

## 1. Observations (user report)

1. Direction-family colors improved perceived visual variety.
2. Blast fragmentation/fading was less comfortable than Classic's persistent illumination. Desired feel is firecracker/balloon `pop`, not merely particles/fade. The user wants a faded circle and ORIGINAL ARROW after explosion for review.
3. Current sound remains simplistic and lacks crisp, startling `啪` transient and escalating cadence.
4. After a wrong Seed, seeing dormant arrows makes it much easier to infer the eventual successful Seed. Unknown whether this is an intended feature or puzzle-depth flaw.

These are genuine internal playtest observations but not externally validated results.

## 2. Verified code facts

In `prototype/chain-shot-v0.3.html`:

- `sound('hit')` fires before `sound('explosion')`; each can allocate two voices, but ordinary events share a 9-voice cap. Under bursts, later explosion layers may be dropped. This is a plausible masking explanation, NOT an audio listening test.
- `explosion` recipe currently uses a 75Hz triangle sweep and 500Hz band-pass noise for ~90–120 ms. It does not prominently feature a very fast bright broadband pop transient.
- Blast fully replaced active nodes by a faint circle plus horizontal mark, losing the original direction. The three stylized fragments and fade convey disintegration more than a sharp balloon-like snap.
- Blast and Classic use the same simulation, so A/B presentation comparisons are viable.
- The existing Solver uses deterministic ray-to-node graph reachability.

Do not claim to have listened to real game audio; these observations combine code inspection and user report.

## 3. Mathematical diagnosis

Let graph G contain an edge A→B if A's ray crosses B. A complete attempt from Seed S activates exactly `R(S)`, the reachability closure.

Because R(S) is closed under outgoing edges, no node in R(S) can reach a node outside it.

Therefore if an attempt fails:

**every successful Seed must lie in the unactivated complement U = V \\ R(S).**

Stronger:

If exactly one Seed solves a level, that Seed cannot have any incoming edge from another node. Otherwise that predecessor would also reach all nodes, contradicting uniqueness.

So a level with a unique successful Seed necessarily features a single zero-in-degree root. This can create a "find the arrow nobody can hit" strategy, without fully mentally simulating the chain.

This insight reflects a property of the rule, not a Solver bug. Don't "fix" it by hiding arrow clues.

## 4. Quantification of current ten levels

We recomputed directed edges from the 10 JSON levels and tested every Seed.

| Level | Wrong Seeds | Wrong attempts leaving 1–2 dormant nodes |
|---|---:|---:|
| 1 第一推动 | 4 | 1 |
| 2 一线分叉 | 6 | 1 |
| 3 折返 | 7 | 1 |
| 4 交汇 | 8 | 2 |
| 5 闪电 | 10 | 6 |
| 6 双环 | 11 | 2 |
| 7 爱心 | 10 | 8 |
| 8 房屋 | 12 | 1 |
| 9 回旋 | 15 | 1 |
| 10 终章 | 17 | 0 |
| **Total** | **100** | **23** |

All 10 levels have 1 successful Seed and that winner is the unique zero-in-degree node.

This is **CALC based on current as-filed V0.3 level data**, not player analytics. It does not measure actual first-click distribution: players' chosen seeds are not uniform.

Especially L5 6/10 and L7 8/10 of *wrong starting choices* leave at most two candidates. The initial generator reward for near-miss may therefore be over-incentivizing immediate deduction, not deep multi-attempt reasoning.

## 5. Decision: Preserve learning, constrain trivialization

- Treat **failure carries information** as a useful feature.
- Treat **near miss nearly always reduces candidate pool to 1–2** as a potential puzzle-quality flaw.
- Do not simply hide activated/dormant evidence, add lives, or punish wrong choices.
- In Blast, preserve faded circle **and original direction arrow** after explosion; evidence must remain available for player-led deduction.
- Add offline metrics:
  - `unactivatedCount(seed)`;
  - `postFailCandidateCount` = unactivated count (a valid upper bound, not number of actual solutions);
  - `P_small_remainder` = fraction of incorrect Seeds leaving ≤2 nodes dormant;
  - count of clear root hints / indegree-zero nodes;
  - graph structure and ease of visual identification;
  - human test: attempts-to-solve, reasoning-first vs trial-and-error, second-attempt choice and explanation.

Target: don't require monotonic difficulty by raw node count; avoid stacking levels where almost every wrong Seed leaves only 1–2 candidates. L5/L7 merit regeneration or replacement after human validation.

## 6. Decision: V0.3.1 presentation experiment (not a new gameplay rule)

Three modes with SAME selected levels and same simulation:

- **A Classic + existing effects/sound** (baseline);
- **B Classic + crisp pop SFX / impact timing** (isolates sound and timing);
- **C Blast + crisp pop / retained directional ghost** (tests removal explicitly).

Do not copy branded samples or effect assets.

### Balloon / firecracker pop

The most salient desired feature is **transient timing and material feel**, not particle count:

- almost instant, broad-spectrum pop (fast attack);
- very short body resonance;
- rapid decay, optional fine crackle tail;
- synced 1-frame white impact and asymmetric tears/shards;
- disappearance after snap, not slow uniform dissolve;
- directional ghost appears immediately after physical pop, at low contrast.

Prioritize the impact voice so bursty ordinary hit tones cannot prevent pop from playing. Cap simultaneous sounds with deliberate grouping or impact prioritization; don't indiscriminately increase volume.

Try 2–3 alternative dry pop timbres and listen on both phone speaker and headphones. Allow use of ORIGINAL recordings or legitimately licensed CC0 audio; don't constrain the team to oscillator-only sounds if those sound synthetic.

References:
- https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Advanced_techniques
- https://kenney.nl/assets/impact-sounds (CC0)
- https://kenney.nl/assets/interface-sounds (CC0)

### Rhythm

Use a short anticipation → hit → chain acceleration → crescendo → closure arc.

No constant full-board shake or stacked explosions that drown causality. SFX should reinforce physical contact; audio tests must be listened to, not just peak-metered.

## 7. Gate and next evidence

Before moving to a new core mechanic:

1. User A/B listens to at least 3 pop recipes in isolation and in 10-node chains.
2. User compares A/B/C on identical levels and reports comfort, clarity, appeal after 5 minutes.
3. Fix/review L5 and L7 post-fail candidate collapse; run one short human playtest without instructions.
4. Observe whether players deliberately reason before first tap and whether subsequent attempts change purposefully.

If sound/visual improve but users continue to blindly tap and finish after 1–2 mistakes, **the problem is puzzle-depth, not insufficient juice**. Then consider a separately gated rule/objective variant rather than continuing to add effects.
