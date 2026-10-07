# Chain Shot — Prototype Design V0.1

> Branch: `design/chain-shot-v0.1`
> Date: 2026-10-07
> Goal: 只验证核心 Pleasure Loop，不验证商业化与长线系统。

## One Sentence

**点一个箭头作为第一推动力，让它触发其他箭头并形成分叉连锁；一次点击点亮全场即通关。**

## Core Pleasure Loop

`观察方向 → 预测 Seed → 点击 → 连锁展开 → 看懂成功/失败 → 立即重试`

核心高潮不是“点箭头”，而是：

**我只做了一个很小的动作，整个系统开始自己运行。**

## V0.1 Rules

1. 棋盘为 7×9 网格。
2. 每个节点只保存一个方向：U / D / L / R / UL / UR / DL / DR。
3. 玩家每局只能主动点击一个 Seed。
4. Seed 激活后沿自身方向发射 Pulse。
5. Pulse 一直运动到边界，不会在碰到第一个节点后停止。
6. Pulse 经过未激活节点时，该节点立即激活并发射自己的 Pulse。
7. 一个节点最多激活一次。
8. 所有 Pulse 消失后结算。
9. 全部节点激活：Success；否则 Fail。
10. Fail 后立即 Restart，可选择不同 Seed。

## Why “Pass Through”

如果射线碰到第一个节点就停止，绝大多数局面会退化为单链路径。

V0.1 要验证的是：

**Local Action → Branching Global Consequence**

因此射线必须能够沿一路触发多个节点，形成自然分叉。

## Non-goals

不做敌人、数字、Buff、技能、障碍物、经济、Meta、账号、联网、排行榜、广告、关卡编辑器、程序化生成器。

## Visual Language

- 深色背景；
- 未激活节点：低亮圆形 + 高可读箭头；
- 激活节点：高亮、扩散环、短暂缩放；
- Pulse：短拖尾光点；
- 连锁越深，声音音高与反馈略增强；
- Success：全场短暂整体闪亮；
- Fail：保留已激活/未激活差异，让玩家能复盘。

不需要角色、美术资产或复杂 UI。

## Five-level Test Ladder

### L1 — Learn
5 个节点。一个明显正确 Seed。理解“光束可以继续穿过节点”。

### L2 — Branch
7 个节点。一次射线触发两个以上节点，第一次出现明显分叉。

### L3 — Near Miss
9 个节点。错误 Seed 也能触发大部分节点，制造“差一点”的重试欲望。

### L4 — Diagonal
11 个节点。加入斜向路径，但不新增规则。

### L5 — Dense Cascade
13 个节点。一次正确点击产生全屏级连锁，用于验证视频高潮。

## Playtest Gate

需要记录而不是口头讨论：

- 首次理解耗时；
- 是否在第一次点击前观察方向；
- 是否看完整个连锁；
- 失败后是否主动重试；
- 第二次是否更换 Seed；
- 是否能解释某个节点为什么被触发；
- 5 局后是否还想继续。

## Kill Conditions

- 连锁看起来像随机烟花；
- 玩家不关心 Seed 选择；
- 错误选择与正确选择的结果差异无法理解；
- 一局答案一眼唯一且没有“差一点”；
- 第一次看完后不想亲自再点；
- 不加第二套系统就没有任何可玩性。

## Backups

### Bounce Merge
`Aim → Bounce → Merge → Goal`

保留，但当前不并行开发。

### Breath Block
`Hold → Expand / Release → Shrink`

保留，但当前不并行开发。

## Next Gate

V0.1 通过后，先尝试只用 **位置、方向、节点数量** 增加深度。

只有这些参数不足时，才允许讨论一条新的最小规则。
