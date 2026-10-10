# Global Pleasure-First Mechanic Scan V4.0｜12 款定向研究

日期：2026-10-10；状态：RESEARCH / NO PRODUCTION GO；官方规则与少量评论研究 + 一个简化策略仿真，尚未逐款完整真人试玩。
方法来源：Color Lines 清盘用户实测 Meta Review（research/minimal-puzzle-scan/COLOR_LINES_CLEAR_BOARD_REAL_PLAYTEST_META_REVIEW_V0.4.md，位于 research/minimal-puzzle-scan-v3-20261010），Route B 目标（main/research/mechanic-principles/route-b-minimal-puzzle-target-v1.0.md）。
去重：先查询 main/research/game-registry/GAMES.tsv 的54条登记，避免重复研究 Color Lines、SameGame、Arrow Out、Endless Peel、Wilmot等；更早的50张截图尚未全量映射，不宣称全局100%去重。
适用目标：无需重美术的2D/轻度益智，固定高复用符号，需有主动继续下一次操作的愿望。原型阶段允许忠实复现规则，产品化另审竞品、知识产权、分发。

## 决策摘要
**两条 RULE_PROBE：Flood-It 的区域扩张/策略、SET 的视觉发现/眼力推理**。
**一条 CONDITIONAL：Infinity Loop 的闭合修复/无打断品质**，先验证是否「思考>机械旋转」，暂不立项。
其他九款含很好的释放因果，但要么与 Arrow Out 高度相邻、要么依赖社交/动作/手工关卡、或有延长压力，保留独立参照，不再反复建议另做。

## 12 个具体源游戏——3层扫描

| ID / 原作 | 必须保留的核心动作与快乐 | 最强反例及目标限制 | 本轮 |
|---|---|---|---|
| play:org.emunix.floodit / Flood-It（Boris Timofeev Android 实例） | 选择目标色，角落已占色块区域吸收相邻同色块；区域一步步单调扩大，眼前选择与未来邻域取舍 | 眼下最多吸收的贪心可能基本够用；有限局策略低；竞品很多/长期流量有限；无端点释放感不代表高留存 | PROBE / SHORT STRATEGY GATE |
| publisher:playmonster/set / SET | 12张符号卡中找到三张在四属性分别全同或全异，发现瞬间明确「啊哈」并刷新新局 | 4视觉维度上手慢、像练习题；单人玩没有竞争节奏；商标品牌/卡片设计不能复制 | PROBE / VISUAL_GATE |
| play:com.balysv.loop / Infinity Loop | 点击旋转连接线段直到全封闭；对象表示规则，收尾的整图闭合很舒服 | 中间重复旋转/逐点劳动，解压但容易无聊；已有大量纯净浏览器/开源实现；官方承认兼顾无限题和升难度不容易 | CONDITIONAL / REPETITION_GATE |
| kongregate:kekgames/unpuzzle / Unpuzzle (KekGames) | 按阻挡顺序从交错方块中移出对象，解除后续阻挡 | 与 Arrow Out、移出类高度邻近；后续 Unpuzzle2 更多轨道、绑定、爆破等机制，题库/教学成本，暂不提纯为新产品 | REFERENCE / ARROW_OUT_NEAR_DUPLICATE |
| linkedin:zip / Zip（LinkedIn） | 一笔画满全格且途经按序数字；一个连续触控动作带来认知完成感 | LinkedIn 有成熟每日分发；有质量的 Hamilton 路径谜题需约束生成与难度评分；初始玩法像拼路线，非自动释放 | PARK / PUZZLE_GENERATION |
| name:drop7 / Drop7（原机制，规则由第三方可交互研究站文档核对） | 按列落数字球，数字=同一连续行/列长度则爆炸，重力引起链式爆炸 | 五次放置新增整行隐藏方块，压力和 Color Lines 同类，隐藏信息/层层计分复杂；不直接作为轻解压原型 | PARK / SURVIVAL_PRESSURE |
| publisher:taito/puzzle-bobble / Puzzle Bobble | 射出泡泡与相同色凑3个消除，悬挂组大面积落下爽感 | 依赖射击瞄准和轨迹/反弹手感，已有高度成熟2D同类、长期关卡内容；可作“剪断支撑→大面积掉落”机制基因 | REFERENCE / RELEASE_GENE |
| ios:id684932119 / Qwirkle (MindWare) | 色彩或形状延长合法线，拼出6格得高分，放置约束明了 | 原版多玩家竞争与长期计分是核心；对一人手机仍有较长回合、没有集体清除，单人版价值未证 | PARK / MULTIPLAYER_SOCIAL |
| nintendo:color-zen / Color Zen (Nintendo) | 通过色块形状触碰与归并，让画面变为目标单色，宁静完整 | 音乐/色彩过渡/手工布局承载很大快乐，静态形状简化可能破坏作品主要感官价值；相近 Flood-It，避免双重原型 | PARK / SENSORY_LEVEL_CONTENT |
| play:com.game.foldpuzzle / Paper Fold (CASUAL AZUR GAMES) | 折叠图案从碎片组成完整隐藏图片，正反馈明确 | 识别图案、折叠层次与3D柔软反馈是主要卖点，几何廉价化会削弱发现内容；大量图案与关卡供给 | SKIP / ART_CONTENT_TRANSFER_LOSS |
| play:com.BuddyMattEnt.ChainReaction / Chain Reaction (Buddy-Matt Ent.) | 放一粒达到临界值爆裂，四向相邻自动触发多级连锁，视觉效果强 | 原作主目标2–8人抢夺棋盘，去掉对抗后可能变无聊的铺垫点击；AI/多人不在本轮 Solo 目标 | SKIP / MULTIPLAYER_CORE |
| publisher:zygomatic/spot-it / Spot It!（Asmodee/Zygomatic） | 两张卡寻找唯一相同符号，快速识别后瞬时确认 | 多人竞速为中心，几十种独立图案、纯单人反应不够可学习的策略，且用户当前希望益智非纯眼力 | SKIP / SOLO_CORE_LOSS |

注：单条游戏 ID 指向某个可信的具体发行/实例，不意味着其他开发商相似标题是同款；后续 registry 保持 canonical ID 不乱合并。
全部官方/一手来源集中于本报告末尾。

## 深挖候选一：Flood-It

原始纯机制：在固定彩色网格，持续切换左上角连通区域颜色，并吸收边界同色连通片，目标用较少操作染满地图。产生最直观的「可见地盘越来越大」：不用逐颗搬球，也不会清到剩下几颗又重新整理。
- **Delta R（表达）**：已是规则与视觉同一语言——颜色即规则，不能靠减美术声称创新。可只给占领区域加清晰一体高亮，但现代竞品已很简约。
- **Delta E（体验）**：一次色彩操作是否有舒适的面积扩张/波纹反馈；关键并非屏幕占满美术，而是玩家预期的边界被吞并。
- **Delta M（不强求）**：优先暂时不加新规则！先验证玩家是否能通过看远一步，做出比每次吃最多更有效的决策。
- **Strongest counter**：颜色区域在九轮左右就全覆盖，随机局后续节奏高度相似，最优玩法未必可在肉眼上学习；不带内容系统会疲劳；市场有诸多早期同款。
- **Next evidence**：先体验原作/两个现代版本各3局，刻意试一次“当前多吃 vs 为下一回合铺路”的选择。若无法产生可解释的反贪心决策或连续3局后只有机械点击，则不做原型。
- **Solo Fit**：2D 单屏，一次颜色点击，全局可预期同步变化，状态完全可实现；约半日至一天的极简 JS 规则对照模型，非成品工期。

### CALC：200个固定伪随机盘粗略策略探针（已运行）
- 7×7、4色、200 seed，线性同余 RNG：初始 v=seed+123456，每抽一次 v=(1664525*v+1013904223) modulo 2^32，取 floor(4*v/2^32)。
- 固定左上起点；贪心每回合选择吸收格最多的不同当前色；另一个两步预判按“下一步最优可覆盖数→当前覆盖数→颜色ID从小到大”选择，直到全部覆盖。
- greedy 平均 9.28 步、median 9；两步前瞻平均 8.655、median 9；在 200 局中两步前瞻优 98、平 95、劣 7（劣说明局部两步启发式不是全局最优）。
- 说明：仅证明简单的未来预判**有条件优势**，不是统计显著结论、最佳算法、玩家能看到的乐趣或产品留存。比起 Endless Peel，其无倒灌新物品的压力是明确结构差异。

## 深挖候选二：SET——不要误判为“给孩子找相同”
- 官方四种视觉维度：颜色、形状、数量、填充状态；对于任意属性，三张所选卡应全部相同或全部不同。共有3^4=81张，不用大量图像素材。
- 核心循环：发现关系 → 立刻确认三张 → 替换并出现新搜索。认知型而非释放型，不需要移动与空走。
- Counter：规则说明虽一句话，玩家需要同时追踪四属性，初次体验可能出现“看不懂→机械找图案→像视觉练习题”的问题，与 Color Lines 的“低龄练习感”风险相反但同样致命。
- Fidelity first：先保留4属性，不能未经测试就改2属性/加入技能。UI 以几何图案独立绘制（不可照搬原游戏牌面/品牌）；发牌保证当前局有至少一组三元匹配，记录首次理解/首次正确发现耗时；无需动画特效体系。
- Next Evidence：先自己玩7–10分钟网页 SET，判断“找到的瞬间”是否真的有欣喜而非只需高度专注；陌生玩家盲测（单人），若多数无强烈正反馈或认为重复视觉扫视疲惫，停止。
- Solo Fit：高，数学出题比手工关卡简单，但**确保可学习难度递进**依然要评估，不拿数学完备等于产品成立。

## 条件备选：Infinity Loop
- 官方 App Store：点击旋转线段连接，避免松散端点，强调无限放松/无时限。官方 Google Play 自述为了“无限关卡+逐级更难+放松”，没有让10万关比10关一定更难；说明内容无穷不是难度有质量。
- 2023/2025 用户评论：原本喜欢的纯粹线段谜题被 XP/奖励动画打断；这是少量已公开用户主观反应，不是全体留存证据。
- 研究机会是成熟产品反向去功能，但目前又已有纯净第三方/开源替代，不能说市场无人满足。
- 最强反例：转完一张牌还有20张，每次判断接线之后只能连续旋转和点击，与 Color Lines 后期机械搬运类似。
- Next Evidence：同一规则的小盘/大盘对照，记录不得不重复点击方向的次数、最后20%的无脑操作量、是否自发再玩。该 Gate 没过，不进入 HTML 原型。

## 红队、决策与注册
- Unpuzzle 与 Arrow Out 同属释放/路径移出类，不能因为读图清楚就推荐改成新“箭头”而复制；Unpuzzle2 还暴露加机制与手工关卡成本。
- Drop7/Chain Reaction/Puzzle Bobble 都有爆炸，但爆炸**发生前需要付出的代价**差异巨大；“有爆炸动画”不是爽感证据。
- Zip 是纯线条谜题的一个非常优雅实现，但 LinkedIn 每日分发和关卡策划明显不能低成本直接移植。
- Spot It 的乐趣很多来自多人竞速，不能因为符号易画就认定单机同样有趣。
- 因此本轮坚持“两证优先 + 一条件观察”，没有新玩法被证明是“下一个 Arrow Out”。
- Kill 通用：连续行为没有可学的有意义取舍 / 主要动作在第三回合起开始变机械、索求复杂手工内容和付费成长系统才保持乐趣 / 玩家不能无需讲解理解基本因果 / 与已有极简竞品没有用户正向差异。
- Product Gate：这些原游戏是受保护的商业作品，不能复制官方商标、素材、独特图案/关卡或源码；忠实规则研究原型不等于可以直接商业上架。

## Verified source links
- Flood-It 规则与简约市场：https://play.google.com/store/apps/details?id=org.emunix.floodit ; https://play.google.com/store/apps/details?id=com.rmaalouf.floodit ; 在线体验与贪心说明 https://absurdtools.com/flood-it/
- SET 品牌/规则：https://playmonster.com/product/set/ ; 在线同规则：https://setpuzzle.com/
- Infinity Loop 原官方 Google Play/Apple：https://play.google.com/store/apps/details?id=com.balysv.loop ; https://apps.apple.com/us/app/infinity-loop-relaxing-puzzle/id977028266 ; 另一个独立网页实现：https://playmemorize.com/infinityloop
- Unpuzzle 原作者：https://www.kongregate.com/en/games/kekgames/unpuzzle ; 后续：https://www.kongregate.com/en/games/kekgames/unpuzzle-2
- LinkedIn Zip 官方：https://www.linkedin.com/help/linkedin/answer/a7445030
- Drop7 规则的第三方详尽复核：https://drop7.dev/learn/rules
- TAITO Puzzle Bobble 原作规则：https://www.taito.co.jp/en/PBEverybubble/gamemodes
- Qwirkle 发行商：https://www.mindware.orientaltrading.com/qwirkle-tile-matching-game-award-winning-strategy-game-for-family-game-night-a2-32016.fltr ; App：https://apps.apple.com/us/app/qwirkle/id684932119
- Color Zen Nintendo：https://www.nintendo.com/us/store/products/color-zen-switch/
- Paper Fold Google Play：https://play.google.com/store/apps/details?id=com.game.foldpuzzle
- Chain Reaction Google Play：https://play.google.com/store/apps/details?id=com.BuddyMattEnt.ChainReaction
- Spot It! Asmodee：https://store.asmodee.com/collections/spot-it
