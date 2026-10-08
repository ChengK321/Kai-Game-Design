# Kai Game Design — Chain Shot V0.1

## Current Design State (2026-10-09)

**Source of truth:** [Chain Shot Master Design State & One-Rule Depth Gate](CHAIN_SHOT_MASTER_DESIGN_STATE_2026-10-09.md).

- Latest experiment: **V0.3.1** (`prototype/chain-shot-v0.3.1.html`).
- Human-preferred design baseline: **Classic + synthesized Hit + Direction-family colors**.
- In-game experiment currently may launch with Pop; use `?audio=synth&mode=classic` for the approved baseline.
- Licensed Pop / Balloon Blast: **HOLD**, not permanently rejected.
- Rule, Solver and curated 10 levels: **frozen pending new evidence**.
- Next: **One Rule depth and failure-learning human playtest**. No V0.4/new systems approved.
- Research integration: [Kai-Game-Lab Game Skills PR #2](https://github.com/ChengK321/Kai-Game-Lab/pull/2) remains open/not merged; methods only, no automatic installation claim.


本分支用于验证 Chain Shot 的核心 Pleasure Loop，不代表完整立项。

## Files

- `CHAIN_SHOT_DESIGN_V0.1.md` — 规则、范围、Playtest Gate、Kill Conditions
- `CODEX_TASK_V0.1.md` — 可直接交给 Codex 的实现任务
- `prototype/chain-shot-v0.1.html` — 单文件 Canvas 交互原型

## Current Decision

- Active Prototype: **Chain Shot**
- Backup: **Bounce Merge**
- Backup: **Breath Block**

当前只验证：**一次点击能否触发清晰、可预测、值得观看的分叉连锁，并促使玩家主动换 Seed 重试。**

不要在 V0.1 增加敌人、技能、数值成长、障碍物、Roguelike、Meta 或程序化关卡系统。

## Playable V0.3

- 双击 `prototype/chain-shot-v0.3.html`：十关、Classic / Blast、三种配色与合成音效。
- `?mode=blast&theme=palette` 指定实验；`?debug=1` 显示开发演示。
- 实现和验证边界见 [CHAIN_SHOT_V0.3_REPORT.md](CHAIN_SHOT_V0.3_REPORT.md)。
- Solver：`python tools/chain-shot-solver.py prototype/chain-shot-v0.3-levels.json`。
