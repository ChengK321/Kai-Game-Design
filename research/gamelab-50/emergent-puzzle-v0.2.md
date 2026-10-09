# Gamelab 50 样本 → One-Rule / Emergent Puzzle 研究 V0.2

日期：2026-10-09｜项目：个人游戏实验室｜状态：研究中｜默认：Chain Shot 不在本研究范围内

## 1. 三个独立概念分支（相互竞争，不合并主线）
- [吞噬滑棋 V0.1](https://github.com/ChengK321/Kai-Game-Design/blob/concept/swallow-slide/concepts/swallow-slide/CONCEPT.md) — `concept/swallow-slide` — WATCH
- [剥剥乐 V0.1](https://github.com/ChengK321/Kai-Game-Design/blob/concept/peel-peel/concepts/peel-peel/CONCEPT.md) — `concept/peel-peel` — HYPOTHESIS，优先测试双端剥离的无尽计分变体
- [翻盘流墨 V0.1](https://github.com/ChengK321/Kai-Game-Design/blob/concept/flip-ink/concepts/flip-ink/CONCEPT.md) — `concept/flip-ink` — WATCH / HIGH-RISK

分支只用于设计、原型与 Decision Log 的独立迭代；结果可终止、可归档，但不能因为建了分支就承诺开发。成熟公共规则沉淀 main，分支特有假设留在各分支。

## 2. Google Play 同类规模：不能简单得出「没人玩」
核验日：2026-10-09。Google Play 显示的下载数字是**累计安装量档位**，无法说明 D1/D7 留存、买量成本、付费 ROI、利润或自然量。
- [Hungry Balls / HYPERCELL](https://play.google.com/store/apps/details?id=com.hungry.balls)：500万+；主要是挖沙物理引导，不是格子吞噬的直接竞品。
- [Rolling Balls Swallowing / zame](https://play.google.com/store/apps/details?id=com.rollingballmomok.rollballswal)：50万+；更接近吞球增长。
- [Ball Run 2048 / KAYAC](https://play.google.com/store/apps/details?id=com.kayac.ball_run)：1亿+；属于滑动数字合并、角色变大，不是本提案的直接验证。
- [Block Blast! / HungryStudio](https://play.google.com/store/apps/details?id=com.block.juggle)：10亿+；说明低动作成本＋长生命周期的空间决策极具市场吸引力，不能归因于单个机制。
事实边界：这些安装数无法检验我们的三款候选是否值得做；低下载量也不能直接证明核心机制失败。产品定位、投放、发行、上线时间、商店曝光和质量都是混杂变量。

## 3. Sudoku 与 2048 不是同一设计范式
- 数独：**静态约束的推理深度**。规则少、约束相互传播，但需要出题、验证唯一解、难度调度。
- 2048：**动态状态机的涌现深度**。有限棋盘＋一次全局操作＋同数合并＋每步新生＋空间资源逐渐耗尽；不依赖手工关卡。官方说明 [2048 Original](https://www.2048original.com/support.html)。
- 2048 并非无前身，原作者承认受 1024 与 Threes 启发。[原作仓库](https://github.com/gabrielecirulli/2048)。
- 此次实验室首发优先：无需关卡流水线的有限空间生存计分。并不是「看起来像数字格」就叫 2048 类游戏。

## 4. 从 50 款中抽出的底层规则积木
A. 接近边缘/端点者才可操作（本草寻秘、本草华章）；B. 本次操作带来局部或跨区域的群体响应（一触即发、九鼎之局）；C. 两块相遇立刻合并/消除（星云穿越、孔明跳棋）；D. 每次操作改变未来可达状态（移星掠形、管道迷阵）；E. 确定性的局部规则会演化出较复杂局面（元胞自动机、兰顿蚂蚁）；F. 空间容纳力形成结束压力（作为候选新添加的生存目标，非原图既有规则）。

## 5. 四个检验门槛（Emergent Puzzle Gate）
1. 单一输入：点或滑，一句话讲清其因果；一分钟内不上教程。
2. 行动收益＋代价：该步带来立即清除/合并，同时使未来局面产生约束或消耗有限空间。
3. 可持续状态变化：不用大量手做关卡，重复动作也不会退化成同一种情况。
4. 可用策略：同一状态下存在明显强弱不同的合法选择，能通过回看解释差别，且不是靠隐藏 RNG 决定。

## 6. 重点假设：双端剥离 → Endless Peel
棋盘为四条同色块队列。玩家点任意端点颜色 C，四条队列从两端连续剥掉所有当前可访问的 C，直到无 C 端点。每回合结束，按照可视且可预期的刷新机制增加少量新块；任一队列超过容量则失败。以得分/存活步数为长期目标。

关键不是“剥离动画爽不爽”，而是“消掉当前颜色是否会**释放/堵住**未来的选择”，并让玩家有风险管理决策。未知：最优操作是否退化为每次只挑清得最多的颜色、是否纯随机决定成绩、刷新规则是否会持续制造公平局面。不得无证据声称已经获得 2048 的深度。

## 7. 必须做的低成本测试
- 用纯逻辑模拟器比较：随机合法选择、当前最大剥离、前瞻1-2回合选择；同一批种子下的生存步数/清除数分布。如果三者无差距，拒绝进入美术开发。
- 用5–8位真人：5秒内是否理解、每一局主动续玩、是否自发发现“为了以后露出某色，眼下不应选最多”的策略。
- 若需增加特殊块、额外动作、关卡工具才产生策略，先判负而非加功能救它。

## 8. Decision Log
- Decision：3 个概念各一个独立分支；主线先记录研究原则与跨项目结论。
- Evidence：50 组截图体现上述抽象积木；官方 2048 规则与 Play Store 累计安装档位支持市场背景。
- Counter Evidence：无当前新玩法真人留存；相邻玩法成功不能迁移成功；过度受《2048》名字锚定的风险。
- Unknowns：哪种操作最可解释、何种机制形成不靠投放的传播、策略深度、端点玩法的低成本广告素材表现。
- Kill Condition：随机策略与真人长期表现接近、玩家缺少自主复玩、需靠功能堆叠弥补薄弱核心。
- Next Evidence：先完成 Endless Peel 的模拟+无说明试玩，再与吞噬滑棋一并比较。
- State：WATCH / HYPOTHESIS，暂无爆款证据。
