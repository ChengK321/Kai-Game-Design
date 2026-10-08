# Chain Shot V0.3.1 — In-game FX Integration Gate

> Date: 2026-10-08
> Status: next experiment approved in principle; not a replacement of V0.3
> Source: user has listened to four crisp FX-Lab samples but cannot yet evaluate real gameplay feel
> Current input: `prototype/chain-shot-fx-lab.html`, `CHAIN_SHOT_FX_LAB_REPORT.md`, `prototype/chain-shot-v0.3.html`

## Decision

Stop polishing the standalone soundboard. Build a controlled *in-game* A/B harness around actual player-chosen seeds and existing V0.3 levels.

The FX Lab already replays L6/L10 with deterministic timings, but scripted replay does not capture player anticipation, a mistaken seed, real-time interaction, retry motivation, or abrupt success/fail transitions.

### Preserve

- V0.3 and FX Lab remain unchanged for regression and repeatability.
- Core cell-step logic unchanged; Solver and 10 levels unchanged.
- Default direction-family colors can be used as the common visual baseline.
- All experimental modes share same levels/Seed/propagation.

### Deliverable

New `prototype/chain-shot-v0.3.1.html` (+ only minimal files needed; no new engine or backend).

If possible, reuse the encoded, licensed audio candidates already inside the FX Lab without creating any network dependency. It is acceptable to keep a small local audio asset folder with documented checksums/licenses, provided opening HTML from file:// works in target browsers. Verify actual behavior instead of assuming fetch() works for file:// local assets.

## Controlled comparisons

Two independent toggles:

- **Audio**: V0.3 synthesized Hit (control) vs selected authentic Pop.
- **Visual**: Classic persistent lit node vs Balloon Blast quick rupture + muted circle **AND original arrow ghost**.

This yields 2×2 combinations. The player's seed selection and round outcome must remain identical across combinations.

Audio developer selector may expose all four licensed sources, but begin with ONE candidate that the tester actually preferred; other samples only for comparison. Preserve mute and overall volume settings.

At minimum, support L6 (dense multi-step with mid-level reasoning) and L10 (18-hit crescendo) and allow switching to all 10 existing levels using normal navigation or debug selection. Make restart and same-seed replay easy.

## Audio integration rules

- Preload/decode sound before first attempted game input when feasible, after genuine user gesture for playback permissions.
- Actual `activateNode`/impact event triggers the sound. Do not drive gameplay from a prerecorded FX Lab timeline.
- Keep sound synced to screen impact, not merely the Seed press.
- Pop is the priority transient, not layered after a two-voice synthesized hit that can consume all channels.
- Preserve natural crisp attack; one-shot may be varied slightly at safe bounded pitch/timbre to avoid machine-gun quality without changing recorded source identity.
- At simultaneous same-tick hits, group if needed for an audible accent, but every activation still renders visually.
- Limit simultaneous voices with a defined priority policy. Don't globally turn everything louder to create excitement.
- Respect mute/stop/reset/page hide; avoid stale queued audio and late stale-promise playback after restarts.
- Match *perceived* loudness as closely as feasible. Peak normalization is not perceptual loudness matching; note remaining uncertainty if no LUFS measurement.
- Keep original sound and sample source/licence metadata; do not include unlicensed source audio or proprietary commercial game sounds.

## Visual integration rules

- Keep current Classic as the visual baseline.
- Balloon Pop: near-instant impact, asymmetric short fragments/ring, immediately replace node with faint circle **plus the original directional arrow**.
- Effects are visual only; `active`, `fired`, Pulse traversal, level result remain unchanged.
- Avoid complex shake, persistent particle clutter, excessive frame time, or thick haze that hides path.

## Test matrix

- Same level + same Seed: audio control vs Pop while visual fixed Classic.
- Same level + same Seed: Classic vs Balloon Blast while audio fixed Pop.
- Compare one correct Seed and one near-miss incorrect Seed on L6.
- Compare full 18-hit cascade on L10 (dense sound test).
- Test on desktop headphones and phone speaker if available, noting which were physically tested.

Automation:
1. Core outcome equality across 2×2 modes and all 10 levels/Seeds vs existing Solver.
2. Stop/restart/mute/toggle: no double-trigger or ghost pending sounds.
3. No network requests; no runtime errors; stable layouts on representative phone/desktop viewports.
4. No clipping is necessary but insufficient for subjective sound quality.
5. Preserve V0.3, solver and JSON unchanged.

## Human gate

The user should perform paired tests with fixed levels/seeds and ask:

1. Does Pop sound like physical contact or like UI click?
2. Does 12–18-hit chain crescendo sound satisfying or noisy/like a machine gun?
3. Is Classic+Pop already sufficiently rewarding without node disappearance?
4. In Balloon Blast, can the original arrow direction be read in the aftermath and the failure cause inferred?
5. Do players want to *choose a seed again*, not only replay the effects?

Make decisions:
- Prefer Classic+Pop if its subjective pleasure and readability equal or exceed Blast.
- Keep Blast experimental if it trades too much readability for spectacle.
- If both feel hollow, measure whether cascade pacing and topology (rather than one-shot quality) are the bottleneck.
- Do not optimize level design or failure-information leakage simultaneously; it's a separate puzzle-depth study.

## Post-work report

`CHAIN_SHOT_V0.3.1_IN_GAME_FX_REPORT.md`:
- mode definitions and user instructions;
- assets chosen and licenses;
- files changed;
- executed browser / Solver tests vs human-audio untested;
- known issues and final human evaluation questions;
- Git commit and push status.
