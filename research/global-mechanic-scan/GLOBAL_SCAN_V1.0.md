# 全球极简游戏机制扫描 V1.0 — 2026-10-09

状态：RESEARCH / DISCOVERY，不等于立项；不修改既有 Chain Shot / Sudoku concept 分支。
仓库：ChengK321/Kai-Game-Design，分支 research/global-mechanic-scan-20261009。

## 真正的问题
不是下一款数独、2048、Arrow Out 或给 Arrow Out 换皮；是发现 1 个自然直观的输入动作，经由可见状态产生未来决策/成长/惊喜，且不依赖高内容成本、重美术或买量。
用四个独立 Gate：原生可读性；规则密度与可学习差别；游戏内反馈/重复价值；分发与一人实现。不能把游戏下载数、Steam 评论数、评论区自述或平台推广流量解读为我们的留存。

## 扫描渠道与边界
A. Google Play/App Store：热门移动轻度游戏、安装档位与相邻竞品。同类饱和度可观察，不能从累计安装推当前 DAU。
B. Poki/CrazyGames：无需安装的短首玩、手机单指适配、点击/拖动/长按可理解的机制；平台热榜不是统一全球排名。
C. itch.io：小规模但可能具备高规则创新的浏览器 Game Jam/实验作品，适合机制原型和开发者复盘；不能将星级评论换算商业成功。
D. Steam：机制深度、完成度、短精品关卡游戏与复玩游戏对照；不能据 Steam 好评推小游戏自然量。
E. 每日谜题平台：固定规则 + 稳定题库/社交分发；需控制分发因素。

## 市场外部核对
Naavik (2026-02-22) 依 Sensor Tower 指标：2025 移动 Puzzle 类 Sort 约 10 亿次下载，部分新细分类型增长；Block 类下载增长、收入集中于 Color Block Jam；Screw 类收入集中，部分玩法依赖高摩擦变现。给独立开发的启示不是直接竞争高买量巨头，而是找独立新机制验证。
https://naavik.co/digest/how-niche-subgenres-are-reshaping-the-mobile-puzzle-market/
Google Play Hexa Sort: 10M+ 累计安装档位，只能证实相邻机制市场基础，不代表独立发行可成功：
https://play.google.com/store/apps/details?id=com.gamebrain.hexasort

## 跨平台机制证据（缩略；去原站核对细节）
1. Domino Grove | itch.io | 两格绑定一起放：单点最优消失，产生布局取舍；自己生成后续难题，分数驱动重玩。
玩家自发描述反复游玩，不能外推留存。作者开发日志：上一项目太复杂、试玩者喜欢「把相同的东西分组」即使非最优，于是围绕自发快乐提炼唯一核心；两格关联比单格自然产生 trade-off；后去掉不合体验的限时。
https://ezra-szanton.itch.io/domino-grove
https://ezra-szanton.itch.io/domino-grove/devlog/846299/domino-grove-development-log
2. Blocky Blast Puzzle | Poki | 一次放置获得当前清行与未来空间损失之间的取舍；每回合三块，用户自己不断制造局面。
https://poki.com/en/g/blocky-blast-puzzle
3. Mini Metro | Steam | 一条线既是直觉连接也是资源配置；新站涌现、原方案逐渐失效；代价是更复杂运营节奏、实时仿真。
https://store.steampowered.com/app/287980/
4. ISLANDERS | Steam | 极简评分式建筑放置，位置决定分数/未来用地；题库依赖较低但美术/范围大于单屏。
https://store.steampowered.com/app/1046030/
5. Stickman Hook | Poki | 单一长按/松开建立物理速度、惯性和下一次落点；玩家动作熟练度提供重复乐趣。挑战手感调参和关卡设计。
https://poki.com/en/g/stickman-hook
6. Öoo | Steam (2025) | 炸弹同一个工具不同用法、无文本引导，产生操作发现；短精品 2–3 小时，依赖关卡制作而非无限复玩。
https://store.steampowered.com/app/2721890/oo/
7. nuworm | itch.io | 简洁运动中发现新行为，50+ 关；体验深度多靠手工关卡。
https://cubestudio.itch.io/nuworm
8. Make Ten | itch.io | 框选和为 10 的数字以消除，短时计分；作者展示极简代码版本，但短代码不等于高质量成品。
https://pancelor.itch.io/make-ten
9. Hexa Sort | Google Play | 同色归整、堆叠反馈，视觉语义直观；市场规模已证、类目竞争和变现模式重，原创微改很难。
https://play.google.com/store/apps/details?id=com.gamebrain.hexasort
10. Is This Seat Taken? | Steam (2025) | 根据角色偏好安排行为，直觉性来自现实座位关系；角色描述、关卡及美术内容负担偏高。
https://store.steampowered.com/app/3035120/Is_this_Seat_Taken/
11. A Little to the Left | Steam | 整理视觉成就易理解，但要 100+ 物件场景，重内容资产。
https://store.steampowered.com/app/1629520/
12. BALL x PIT | Steam (2025) | 碰撞反弹 + 融合增效；反复反馈强，但实际成功依赖英雄、升级、基地、内容系统；不照搬完整体量。
https://store.steampowered.com/app/2062430/
13. Arrow Escape / Screw / Sort | CrazyGames | 释放阻挡、分类、拆卸等认知直观的机制持续热门；已强同质化。
https://www.crazygames.com/c/puzzle
14. Level Devil | Poki | 操作目标极清晰，但有意误导/改变熟悉规律；靠惊喜和大量关卡，不符合静态可预期性作为通用设计标准。反驳「所有好游戏必须规则完全可见」。
https://poki.com/en/g/level-devil

## 提炼的三条非互斥机制家族 (Rule Atlas 追加研究标签)
A. **当前收益 + 自造未来约束**：Domino Grove / Blocky Blast / Mini Metro / ISLANDERS。好局面由操作逐渐塑造；最符合单人工作室追求的低关卡成本，但依赖准确可感知的策略差异。发现点：强制绑定两个对象、有限空间、长期风险。
B. **身体直觉 + 操作熟练成长**：Stickman Hook、相关弹跳/物理；不是数独推理而是触屏释放和动量预测。手感/反馈/设备延迟是主要门槛。
C. **一动作多用途 + 逐关发现**：Öoo、nuworm、Baba Is You（后者复杂度更高）。可以做出强 aha 时刻，却很容易需要大量手工关卡，不等于低成本长期运营。
其他参考：D. 天然可读的整理/释放（Hexa Sort、Arrow Out），学习容易但平台同质化重；E. 惊喜违背预期（Level Devil），可成功但需大量设计内容；不能武断排除。

## Decision
最值得进行低成本探索的是 A：动作一方面有立刻收益，另一方面自然制造下一步难题，不需事先画上百关，且画面上直接暴露收益与代价。
B 作为不依赖推理的独立赛道；C 作为机制发现参考，不把手工关卡游戏错误地写成可自动量产的十秒无尽游戏。
不因 Domino Grove 优雅而直接复制「双格颜色匹配」；已有具体产品会造成原创性不足。把它当机制实验对照组。也不能将 Endless Peel 直接视作已赢，只存在策略模拟和待办真人测试。

## 竞争/反例
- 如果仅做「Sort/Screw/Out + 新皮肤」，较强发行商可更快买量/迭代，规则上的区分不足。
- A 中随机刷新的不可预测性可能让人感觉全凭运气；实现后须对随机/贪心/一步前瞻策略运行固定种子对照；再做真人重复游玩测试。
- B 需要物理手感调参，触屏操作失误可能超过玩法乐趣。
- C 玩家前 5 关可能觉得神奇，但制作 100 关过高，不符合现有个人项目主线。
- 优雅不是商业成功充分条件；不同平台发行和触达不同。

## 可执行下一步（非开发承诺）
1. 亲自玩 5 款对照：Domino Grove、Stickman Hook、Öoo demo、nuworm、Blocky Blast；5–10 分钟/款。分别记录是否不看教学就理解、15 秒首个正反馈、同一动作的深层用途、局面变化、五局后仍想重玩。
2. A 赛道只做三个「纯规则小模型」：单元可自由放置 vs 双元绑定放置 vs 端点受限释放；比较可学习策略差距与自造难题，避免直接立项换皮。
3. B 只做一次按住/松开与速度控制的基本手感实验；不先做整套关卡。
4. 若没有一个自然画面能在 5 秒解释动作、并让用户自行发现一条策略，则关闭当批方向，不追加机制救活。

## 记录模板
Mechanic Family | Natural Affordance | Core Pleasure | Immediate Gain | Self-created Constraint | Freshness / Prior Art | Solo Content Cost | Evidence | Strongest Counter | Next Evidence | Kill | State
所有未经真人验证的新产品假设统一 WATCH。成熟共通原则归 main，概念先驻 research 分支。
