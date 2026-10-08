# Chain Shot V0.2 — 视觉、音乐与具象图案实验提案

> Date: 2026-10-08
> Status: PROPOSAL / awaiting prototype comparison, not production-approved
> Scope: Chain Shot V0.2 (no new gameplay rules)
> Companion: `CHAIN_SHOT_V0.2_PLAN.md`, `CODEX_TASK_V0.2.md`
> Reference class: 《一箭又一箭》、Google Play 的 Arrow Out / Arrow Escape 图案关卡

## Decision framing

不要把“复制成功作品的美术/布局/音乐”当任务；真正目标是让 Chain Shot：

1. 第一眼像一个完成度高的休闲小游戏；
2. 输入和因果链更可读；
3. 成功时的分叉级联更有节奏；
4. 关卡不因追求图案而丧失策略性。

借鉴作品的视觉层级、留白、布局/交互节奏、音效功能；不照搬独特素材、旋律、图标、美术资源、现成关卡图案和品牌名称。

## Critical distinction

《一箭又一箭》/ Arrow-Out 类型：解锁箭头的移出顺序；箭头与线段构成障碍，已移出的箭头消失。

Chain Shot：只点一次 Seed；静止箭头触发 Pulse 并分叉传播；发射后的节点保持点亮。

借成熟产品的表达法，不偷换核心玩法。不要给 Chain Shot 增加“挡住则不能发射、生命值、箭头滑出”等另一套主规则。

## Evidence and caution

- Google Play `Arrow Puzzle: Arrows Out` 开发者商品描述明确：心、星、猫、房屋、笑脸等可识别的箭头轮廓。该应用所见下载档位约 500+，只能证明表达存在，不证明该特定产品成功。
  - https://play.google.com/store/apps/details?id=com.teksxt.games.gamearrows
- Google Play `Arrow Escape Puzzle` 开发者描述：苹果、猫、火箭、船锚等图案，列出 43 种形状与 1000+ 关；所见下载档位约 5K+，不能直接推导商业成功。
  - https://play.google.com/store/apps/details?id=com.codeforge.arrowescape
- Google Play `Arrow Escape: Maze Puzzle Out` 列出 1M+ 下载，说明这一大类具备市场触达，但不能证明图案关卡、美术或配乐单独贡献多少。
  - https://play.google.com/store/apps/details?id=com.arrow.puzzle
- 现有公开资料多是商店文案/截图，未独立验证《一箭又一箭》原版完整配乐和具体数值表现；不把参考音效说成已经听过的事实。

## Visual direction: Calm Before, Spectacle After

目标：观察时安静、触发时清楚、连锁后惊喜。

### Before the tap

- 暖灰/奶油白底为主方案，对照现有深色霓虹版，不预判哪一个更好；
- 深色单色箭头，方向/路径对比清楚；
- 不展示过多按钮、数值、无意义玻璃拟态 UI；
- 用“节点位置”产生易认出的整体轮廓：心、房屋、闪电；
- 首屏图案不能占满安全区或压缩触控目标。

### During cascade

- 被触发的箭头颜色递进且保留高对比箭头方向；
- Pulse 是可追踪的线段/光迹；永远从真实节点出发；
- 每次节点激活有 50–90 ms 可见反馈，避免所有节点同帧爆光；
- 连锁后期增加微弱的画面规模感，不用频繁震屏掩盖因果；
- 点击时能看懂箭头为什么响应，不把分叉变成随机烟花。

### Result

- 激活节点形成完整轮廓，可有轻微“完成图案”的明暗变化；
- 错误 Seed 保留已激活 vs 未激活的区分；
- 不新增“收集图鉴、填色任务、拼画奖励”等第二条目标线。

## UI layout (portrait first)

建议初版按视觉区域分层，而不是写死设备像素：

- 顶部约 10–14%：Level / 进度 / 静音；
- 核心画布约 65–72%：构图居中、大留白、自适应大小；
- 底部约 14–20%：一句提示 / 重新开始；下一关仅成功可用；
- Demo 按钮只放开发调试模式，正常玩家入口隐藏；
- 最小点击区域建议不小于 44×44 CSS px，密度增加时放大画布或减少节点，不牺牲手感。

## Audio direction: music is a pacing system

不复制任何原作旋律、音源或音效文件。

V0.2 不需要先做长 BGM；可以 A/B：

**A. Sound-only**
- Seed：短、干净、有实体感的启动音；
- 每次激活：同音色低强度音阶；
- 分叉密集时音高轻微变化，但限制并发混音；
- Success：0.4–0.8s 的短和弦/落点；
- Fail：短、克制的低音，不制造挫败感。

**B. Ambient + sound**
- 轻氛围、低音量、可静音；
- 动作前给空间，级联开始时临时下压 BGM；
- 不中断思考；
- 所有音色可用 WebAudio 合成，无版权/加载依赖。

移动端从真实用户手势恢复 AudioContext；关闭声音偏好本地保留即可，不引入后端。

## Shape-based level generation: mechanic first, silhouette second

**禁止直接照着图案填箭头，然后宣称关卡有策略。**

推荐离线两阶段：

1. 从极简二值图案或控制点采样候选格位，得到 `shapeScore`；
2. 给这些格位分配 8 向箭头；
3. 运行已有 V0.2 Solver，统计 `solutionCount`, `reachRatio`, `nearMissCount`, `cascadeDepth`, `branchEvents`；
4. 同时满足图案识别和逻辑门槛才保留；
5. 最后人工检查手机端可读性与玩后感。

当二者冲突时：**可推理性和节奏 > 图案完美程度**。

不要为精确重建猫脸而加入密集节点、曲线箭头或大量新元素。

## First experiment

开发三种`外观/构图`，玩法规则与交互完全一致：

- **Control**：现有 V0.1 暗色节点自由排列；
- **Visual polish**：同一逻辑棋盘，采用新 UI/声音/动效；
- **Silhouette**：基于新 UI，把关卡布置为玩家大致能认出的心/房屋/闪电轮廓，同时 Solver 保证难度可比。

尽量匹配节点数、正解数、最大深度、near miss 比例。

记录：
- 未点击前对图案的识别；
- 首次点击前是否理解方向和目标；
- 是否在前 5 秒感到想点；
- 级联因果是否更易理解；
- 错误后是否知道改选什么；
- 自发重试情况；
- 连续 5–10 关后的体验；
- 手机实测的方向/点击误操作。

记录 A/B/C 的真实差异，不能因为更像成熟产品就预设 B/C 胜出。

## First milestone / Codex order

1. 保持核心传播逻辑完全不变；
2. 实现 Solver 并校验关卡；
3. 将渲染、音效与关卡数据拆为少量清楚函数；不要引入框架；
4. 用一个主题开关实现轻色/暗色对照；
5. 用 3 个可识别但不强求完美的轮廓试关，并记录 Solver 指标；
6. 真实手机试玩，再决定是否推广到 10 关。

## Kill / Change conditions

- 图案更好看，但需要牺牲明显的 Seed 差异；
- 轮廓增加了看图兴趣，却让人不再认真看方向；
- 箭头密到点不准或方向看不清；
- 音效“热闹”但掩盖层级和因果；
- 玩家愿意看录屏，却不愿亲自试不同 Seed；
- 需要新规则/额外 Meta 才能让图案关卡持续成立。

## Summary

**学习 Arrow-Out 家族的“视觉可读、具象轮廓、轻 UI、操作反馈节奏”，继续坚持 Chain Shot 独有的“一次 Seed → 分叉级联”。**

视觉不是 V0.2 的替代任务，而是需要与 Solver 一起验证的表达变量。
