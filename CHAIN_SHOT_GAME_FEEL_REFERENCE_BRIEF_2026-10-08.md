# Chain Shot — Reference-Driven Game Feel Brief

> Date: 2026-10-08
> Status: Active research / next experiment proposal (not code approval)
> Context: After V0.3 internal playtest, current synthetic sound and three-fragment Blast were not satisfying; Classic felt more comfortable.
> Goal: Stop adjusting vague adjectives. Use observed, licensed reference material and controlled A/B tests.

## 1. Decision

Work via **Reference → Breakdown → Authorized Asset → Small Audition → Same-Level A/B → Integrate**.

Do not recreate recognisable proprietary sound files/visual assets by ear or copy screens. Reuse game-feel principles and independently licensed assets.

## 2. Reference cases

| Reference | What to study | What NOT to copy |
|---|---|---|
| Peggle / Peggle Deluxe | Per-hit audio hierarchy, pitch progression, a distinctly staged end-of-level release | Actual PopCap samples, music, branding, UI |
| Juicy Breakout (open source) | Anticipation, easing, impact, squash/stretch, particle timing, trails, persistent state | Wholesale port of Flash/AS3 game or unrelated systems |
| Puzzle Bobble / bubble popping games | Crisp material pop and small-object disappearance with concise readable response | Character art, recognizable music/sounds, levels |

References:
- https://www.gdcvault.com/play/1016487/juice-it-or-lose
- https://github.com/grapefrukt/juicy-breakout
- https://store.steampowered.com/app/3480/Peggle_Deluxe/
- https://www.theguardian.com/technology/gamesblog/2012/aug/08/popcap-secrets-of-game-design

## 3. Sourcing: shortlist of reusable CC0 materials

All licences must be re-checked at actual download; preserve a local attribution/source record, even where optional.

Audio:
- Real balloon pop candidate 1, CC0: https://freesound.org/people/Breviceps/sounds/458398/
- Real balloon pop candidate 2, CC0: https://freesound.org/people/Lukeo135/sounds/563197/
- Kenney Impact Sounds, 130 sound files, CC0: https://kenney.nl/assets/impact-sounds
- Kenney Interface Sounds, 100 sound files, CC0: https://kenney.nl/assets/interface-sounds

Visual:
- Kenney Particle Pack, 80 files, CC0: https://kenney.nl/assets/particle-pack

Licence confirmation: https://kenney.nl/support

Do not pretend a file was downloaded, listened to or tested without actual verification.

## 4. Soundboard first, gameplay second

Before changing Chain Shot again, create an **audio + pop audition page**. The simplest useful version has:

- three curated pop samples (dry balloon, brighter cracker-like, soft bubble), with clear source/licence;
- playback of ONE hit and a fixed 12-hit cascade using the same timeline;
- playback on/off comparison for existing synthesized hit;
- fixed and reported loudness, clipping limiter and polyphony strategy;
- ability to toggle SFX-only vs SFX+light low-frequency/body layer;
- mobile playback and desktop headphones test.

Do not create a music sequencer / generic sound editor.

Sound event order must be *impact prioritized*: the transient pop is the audible primary event; hit / tonal layer must not occupy all voices before pop. Current V0.3 calls `hit` before `explosion` within a 9 normal-voice cap, which may starve the latter during bursts.

Listen before deciding which clip to ship. Avoid continual pitch rise becoming shrill, and avoid repeated identical samples sounding like a machine gun.

## 5. Animation benchmark

Make just two alternatives using the EXACT SAME simulation and level:

A. **Classic+Pop**: original arrow remains bright; impact flash and crisp pop; no disappearance.
B. **Balloon Pop Blast**: node snaps/ruptures almost instantly, releases a few asymmetric tears/sparks; replace with a low-contrast circle **and the ORIGINAL arrow direction**.

Suggested starting timing (not empirically validated):
- anticipation/compression: 30–60ms;
- actual rupture/white flash: 10–20ms;
- travel/shards decay: 80–150ms;
- ghost state thereafter.

Use rapid material breakup; avoid 200ms gradual fade with three repetitive rotating wire fragments.

Priority hierarchy:
1. causal readability and traceability;
2. perceived physical impact;
3. pleasant chain rhythm;
4. total FX quantity (last).

Try one authentic pop sound synchronised to one physical rupture *before* adding more screen shake.

## 6. Controlled experiment / Gate

Keep the same existing levels and logic. Do NOT change the solver, rules or level generation in this iteration.

First validate on a representative medium-difficulty board, then one 18-node dense board.

Compare:
- Existing Classic / baseline
- Improved Classic+Pop
- Balloon Blast+original-direction ghost

Ask players to describe, without leading:
- Which hit felt best and why?
- Could you identify which original arrow triggered which?
- Would you play another board or only replay the animation?
- Was the dense chain unpleasant or muddy (phone speaker as well as headphones)?

If Classic+Pop is as satisfying as Blast, prefer Classic and remove Blast from the default experience.

## 7. Avoid these costly paths

- No generic audio middleware or complex timeline editor.
- No engine migration solely for particle effects.
- No real-time AI generation of sound or VFX.
- No copied commercial samples from gameplay videos.
- No changing the core mechanics and visual effects simultaneously.
- No 10-level repolish until the single-board A/B produces a clear gain.

## 8. Link to puzzle-depth

The post-failure candidate-set collapse identified in `CHAIN_SHOT_V0.3_PLAYTEST_REVIEW_2026-10-08.md` is a separate mechanic/level-structure issue. Do not mask it with effects; run separate puzzle-depth validation after the reference-driven presentation comparison.
