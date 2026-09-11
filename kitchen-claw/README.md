# 《抓菜上桌 / Kitchen Claw》设计工作区

分支：`design/kitchen-claw-v0.1`

当前阶段：**核心玩法定义 + 首轮10关纸面验证 + 视听方向设计**。

## 一句话产品定义

> 玩家用摆动钩爪从层层遮挡的菜堆中抓取食材，既要完成当前订单，也要把被迫提前抓出的菜合理放入有限备菜台，为后续订单创造连锁上菜机会。

这不是“黄金矿工换皮”。真正的核心是：

**Claw Timing × Occlusion Puzzle × Future Order Planning × Limited Buffer × Chain Serving**

## 当前文档

1. [00-product-thesis.md](./00-product-thesis.md) — 产品定位、三跳、差异化、为什么可能适合微信小游戏。
2. [01-core-loop-and-systems.md](./01-core-loop-and-systems.md) — 核心循环、遮挡、抓取、备菜台、订单、菜堆变化、Combo。
3. [02-first-10-levels-v0.1.md](./02-first-10-levels-v0.1.md) — 前10关完整验证梯子。
4. [03-art-ui-direction.md](./03-art-ui-direction.md) — 美术、构图、角色/菜品表达、UI与反馈。
5. [04-music-and-sfx.md](./04-music-and-sfx.md) — BGM、节拍、抓取/上菜/连锁音效系统。
6. [05-progression-and-content.md](./05-progression-and-content.md) — 长线章节、特殊菜、餐厅主题、难度扩展原则。
7. [06-social-and-monetization.md](./06-social-and-monetization.md) — 微信社交、Daily Challenge、激励广告、商业化边界。
8. [07-prototype-and-validation.md](./07-prototype-and-validation.md) — V0.01原型范围、指标、风险与Kill Criteria。

## 当前设计红线

- 操作简单不等于系统简单；首版只允许“点一下抓”。
- 主要乐趣是“抓什么”，不是“能不能精准点中”。
- 当前订单与未来订单必须同时可见，否则前置规划不存在。
- 抓错不应立即惩罚；它应该成为未来资源或占用缓冲空间。
- 菜堆变化要带来可预期但不完全静态的局面重构。
- 首版不要加入经营装修、Roguelike、角色养成、大量特殊菜等外围系统。
- 如果玩家不能自然体验到“为了当前单挖障碍 → 障碍恰好服务下一单 → 连锁上菜”的顿悟，本项目不进入正式孵化。
