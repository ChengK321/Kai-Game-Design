# Route B V3.0｜极简规则驱动休闲益智：12 款定向提纯扫描

日期：2026-10-10
状态：官方/开发者页面与商店信息检索初筛（没有逐款亲自玩完整局，也没有玩家留存数据）
搜索目标依据：main 的 research/mechanic-principles/route-b-minimal-puzzle-target-v1.0.md
去重依据：main 的 research/game-registry/GAMES.tsv（开始扫描时 42 条）。此前 Color Lines、Triple Town 等作品不在已登记 42 条中；以前从其他游戏抽象出的合并/空间机制属于机制层相似，不能混同具体作品重复。
本轮有意不深扫已在登记的 2048/Arrow Out/Block Blast/Flow Free/Screw Jam/Wilmot/Sandtrix 等。
原型阶段可忠实提纯并独立实现，不要求机制创新；正式发行仍需独特价值与知识产权检查。

## 结果
- 3 个 PROBE（其中第三个存在必须先过的出题质量 Gate）
- 7 个 PARK（保留来源与再审条件，不作为当前原型）
- 1 个 SKIP（当前关卡生产机制不适合）
- 1 个 REFERENCE（已极简，归为成熟对照，不立刻另造一版）
该状态只表示 Solo Route B 的**本轮研究处置**，不代表原作优秀程度。12/12 都需记录去重 ID。

## 12 款一页扫描表

| Game | 原作真正操作/必留限制 | 可去掉/最便宜载体 | 内容与实现风险 | 决策 |
|---|---|---|---|---|
| Color Lines / Lines 98 | 9×9 上移动可达的球；五颗同色成线消除；未消除则出现三球；空间逐渐挤满 | 圆点/色块、点选起点终点、短移动/消除反馈；可删木质贴图/主页/社交/道具 | 颜色数、补球、公平性/预告位置导致难度陡变；单局时间与无尽压力需调参 | PROBE |
| Triple Town | 6×6 放置随机对象；三枚以上正交相邻同级合为下一等级；保留空间压力 | 4–5 级数字或几何形状；先不做熊/城堡风景/商店/体力等外围内容 | 若去掉升级层数/随机约束，会只剩合并动画；特例与平衡需验证 | PROBE |
| KAMI 2 | 改变一个相邻连通色块区域的颜色，使整盘变一种颜色，追求最少操作 | 平面色块及区域涂色波纹；可删纸艺/音乐/故事/社交和关卡地图 | 官方 100+ 手工谜题和 UGC，说明题库高质量并非免费；乱涂不可替代有意义解题 | PROBE-CONDITIONAL |
| I Love Hue | 交换色块，使渐变谱恢复顺序 | 渐变色矩形和少量固定锚点 | 核心感知恰恰依赖精确色彩设计、显示屏色彩/辨识能力；原作已经非常纯粹 | PARK |
| Unblock Me | 固定朝向的车/木块沿单轴滑动，给目标块腾出出口 | 纯色矩形、拖动、阻挡反馈 | 官方 18,000+ 题，如何生成经过难度验证的有趣谜题是隐藏开发成本 | PARK |
| Hexcells Infinite | 观察邻近计数/约束，推导哪些六角格有内容 | 正六边形、两状态与数字提示 | 原作有 random puzzle generator；复制表面容易，高质量纯逻辑题生成验证困难，且与数独研究接近 | PARK |
| Tents and Trees (Frozax) | 每棵树旁一帐篷、帐篷不接触、行列数字配额 | 网格+两符号 | 保证唯一解和无需猜测，难度区分，隐藏题库成本 | PARK |
| Nonogram.com | 按行列分段数字还原二值图案，完成时揭示图像 | 数字线索+黑白格子 | 随机图案未必好看且可能不适合逻辑求解；成熟玩家预期图片完成感 | PARK |
| Hook (Maciej Targoni) | 顺序拆除挂钩，避免互相阻碍 | 线条/开关极简图 | 原作已有极简视觉，官方 60+ 关，随着关卡引入多种机械开关，抽走则深度减少 | SKIP |
| Two Dots | 拖动连接同色点、合成封闭方形可产生大规模消除 | 几种色点+路径拖动+最小消除动画 | 原作额外关卡目标、道具、成长较重；去掉以后是否有足够复玩与目标？ | PARK |
| SameGame | 点击连通同色群消除；上方下落、空列左移，争取清空/高分 | 纯色方格+点击+下落反馈 | 原版机制本来就极简；与已研究 Endless Peel 同属去除颜色组后空间变化，但访问约束不同；纯仿制差异弱 | REFERENCE |
| Hashi: Bridges (Conceptis) | 数字岛屿之间画 1–2 桥，无交叉，全部连通且满足岛屿计数 | 点+数字+直线 | 纯数学不需重美术，但唯一解、无猜测及符合手机指尖操作的出题难度不低；和数独约束研究高度接近 | PARK |

## 证据（优先原作者、发行商、游戏平台原文）
1. Color Lines 98 现代发布者：https://play.google.com/store/apps/details?id=com.numen.lines ；经典规则详细验证：https://lkforge.com/games/lines/ （注明本轮重点研究基础规则而不是该页智能提示功能）
2. Triple Town 官方详细玩法说明：https://support.spryfox.com/hc/en-us/articles/219104828-How-to-play-Triple-Town
3. KAMI 2 开发者商店：https://play.google.com/store/apps/details?id=com.stateofplaygames.kami2 ，以及 Steam：https://store.steampowered.com/app/3414340/KAMI_2/
4. I Love Hue 官方上架页：https://play.google.com/store/apps/details?id=com.zutgames.ilovehue
5. Unblock Me 官方上架页：https://play.google.com/store/apps/details?id=com.kiragames.unblockmefree
6. Hexcells Infinite 作者 Steam 页：https://store.steampowered.com/app/304410/Hexcells_Infinite/
7. Tents and Trees Frozax 官方：https://play.google.com/store/apps/details?id=com.frozax.tentsandtrees
8. Nonogram.com 开发者上架页：https://play.google.com/store/apps/details?id=com.easybrain.nonogram
9. HOOK 作者 Steam 页：https://store.steampowered.com/app/367580/Hook/
10. Two Dots 官方：https://play.google.com/store/apps/details?id=com.weplaydots.twodotsandroid
11. SameGame 具体应用举证：https://play.google.com/store/apps/details?id=com.george.samegame ；经典机制非该作者首创。
12. Hashi (Conceptis) 官方：https://play.google.com/store/apps/details?id=com.conceptispuzzles.hashi

## 排序与可验证原型定义

### #1 Color Lines｜忠实最小玩法
- V0：9×9、7 色、5 同色成线消除、无成线每回合补 3 球、沿空格可达路径移动、满格失败；如原作对下一批颜色提供提示则基线保持对应可见度，不随意隐藏以制造难度。
- 至少要保持“移动路径不能穿过其他球”，这使其不只是把颜色换位置，且产生与已做的 Endless Peel 不同的可学决策。
- 可删：所有非必要包装、商城、辅助道具、花哨图形；不可删：路径限制、成线消除、新球压力和最基本位置反馈。
- 原型预计 1–3 天 AI 辅助（估算，尚未开发）；真正待证：玩家能否预测哪个位置会堵住未来通路；新球随机性是否压过策略；重复玩 5 局时是否仍有不同决策。
- Kill：需要删除可达路径才能做到触屏方便，或随机补球令策略差距不可学习；从已存在的现代纯净版本中获得的体验改善为零。

### #2 Triple Town｜不做城镇，仅保留递进合并
- V0：6×6、下一枚图形预告、相邻三合一、4–5 级形状、满盘结束，最小合并动画；先不引入熊、机器人、商店/能量。不能把“越高级越稀有”的成长目标去掉。
- 与 2048 的区别：决定精确的落点而非全局四向滑动；相邻三个合并与空间局部连锁，三消会释放位置。但这不是原创。
- 若去掉熊/仓库/道具后还存在可学习布局策略，则通过；若相同局面只能凭后续随机掉落碰运气，或者玩家只重复点亮一处大合成却没有未来选择，停。
- 时间估算 1–3 天原型；验证 5 局后是否愿意追求更高级形状，而不是只为了合并动画继续。

### #3 KAMI 2｜必须先验证生成题目
- 只考虑极简平面区域染色，保留相邻区域合并与最少步挑战，不复制原作手工关卡或纸艺。
- 拟用小网格/连接区域生成有限集合的谜题；必须穷举/搜索验证目标最少步数，区分唯一最短解与存在多个等价最短解，并测试人类可读的可解路径。不要把随机着色当成好题。
- 1 天以内的纯规则/纸面出题测试 Gate：10 道候选中能否找到多个推理路径不同且不需猜测的谜题；不能就停，不进入完整 HTML。
- 原作上百万个玩家自创谜题的官方声明只能说明 UGC 的存在，不能证明程序化自动生成足够好。

## 非首选 9 款为何不继续做
- Unblock Me / Tents and Trees / Hashi / Hexcells / Nonogram：题库质量、唯一解、难度递进，开发量隐藏在题目生成与逻辑验证里。
- I Love Hue：用色彩本身就是核心体验，没法“去美工”却不掉分；原作已近极简。
- Two Dots：单个操作可以保留，但长期回访可能依赖大量不同的关卡目标和消耗系统。
- Hook：已经是经典极简作品，去掉关卡引入的机制后只剩简单顺序拆除。
- SameGame：当作极简对照游戏而不是再次开发；若之后证明与 Endless Peel 的“可操作端点”存在价值差异，重新考虑。

## Red Team
- 商店下载与 Steam 评价不是单一玩法成因，尤其用户习惯、发行、广告、关卡都影响结果；不能把累计下载当最近活跃/留存。
- Color Lines 已有极简的独立移动/网页版本；我们的 V0 可作为“基础体验对照”和技术/研究学习，但不应直接上架商业化。
- Triple Town 与 2048 在高层都属有限空间合并，虽然操作差异大，但这不足证明新用户会转向我们的版本。
- KAMI 2 与 I Love Hue 已经用画面直观表达规则，简化视觉可能只让体验倒退。
- 1–3 天只是理想可试玩预算；移动端触控、QA、画面感与生成器成本均可能更高。

## Decision Log
Decision：按 Route B 定向轻度益智原则完成 12 款初筛。No production GO. 主推荐 Color Lines，副推荐 Triple Town；KAMI 2 仅通过出题 Gate 后才成为第三可玩原型；其余记录原因，不重复深扫。
Evidence：上述官方/一手来源，规则与内容规模为 FACT；实际去美术后是否仍然快乐属 HYPOTHESIS。
Counter：成熟极简竞品已经覆盖，忠实原型暂不解决商业差异化；手工题库供给风险；数学存在解不等于人类有趣。
Unknown：真人连续 5–10 局的复玩动力、策略差异是否超过随机、手指操作真实舒适度、抽象图形是否丢失原作感性奖励。
Next Evidence：用户先亲玩 Color Lines 与 Triple Town 原作 5–10 分钟，记录首玩理解、关键收益、重复意愿；择其中一款做小而忠实的 HTML V0，设置同种子对照、非诱导真人试玩。KAMI 2 先做离线出题质量测试。
Registry：全局事实源 research/game-registry/GAMES.tsv on main，不在单个研究分支另建游戏登记簿。
