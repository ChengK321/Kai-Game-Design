# Kai Game Design — Chain Shot V0.1

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
