# Route B｜全球玩法反向提纯扫描 V2.0（12 新样本）

日期：2026-10-09
状态：RESEARCH / 文献初筛；未实际逐款试玩、未做真人留存实验、未启动原型。
准入规则：2D / 低成本平面化优先，3D 最多两款作例外边界检查；一人实验室原型以1–3天为工作量假设，原则上不超过1周；不可把核心编码难度当作完整体验开发成本。
去重依据：仓库已有 GLOBAL_SCAN_V1.0（14个机制/来源条目）、MECHANIC_DISTILLATION_V0.1、ROUTE_B_2D_FIRST_V0.3。第一轮尽量避开 Domino Grove、Stickman Hook、Mini Metro、Öoo、Blocky Blast 等旧样本；已有 50 张截图的完整归档索引尚需后续补全，不声称全部去重。

## 样本简表
状态：PROBE=有明确最小验证任务；CONDITIONAL=保留条件性尝试；PARK=不做原型但可复审；SKIP=目前 Solo/市场/机制 Gate 不通过；REFERENCE=重要机制对照。

| Key | Source | 来源/范围 | 源游戏核心快乐（可证实操作） | 反向提纯到最轻载体 | 最大反例 | Gate/Status | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| steam:2546310 | Sandtrix+ / Sandtrix | 2D；itch/Steam | 规则形状落下变成颗粒，像素连通同色消除 | 低分辨率颗粒棋盘，单动作放置，引力自动变形；重点观察是否发生有意义的二次布局 | 原作已极简；CA性能/边界体验/相似竞品；仅变形不必然有新策略 | RULE_PROBE / PRIOR_ART | https://msky-dev.itch.io/sandtrix |
| steam:839870 | Wilmot's Warehouse | 2D；Steam | 玩家自定摆放/分类、再迅速取回指定商品 | 12-24类符号自主整理后抽检，单指放取；不用完整仓储搬运 | 无语义的几何符号可能失去分类乐趣；记忆任务可能无复玩深度 | RULE_PROBE / REPRESENTATION_RISK | https://store.steampowered.com/app/839870/Wilmots_Warehouse/ |
| steam:3244220 | A Game About Digging A Hole | 3D例外；Steam | 挖掘→可见形状改变→资源→卖出升级→探索地下秘密 | 2D剖面点划挖掘、少量可见/未知矿层，检查“揭开下一层”是否足以驱动操作 | 大幅剥离升级和叙事后没有持续目标；内容/揭示资源可能不可省 | CONDITIONAL / HIGH_REWARD_CONTENT_RISK | https://store.steampowered.com/app/3244220/A_Game_About_Digging_A_Hole/ |
| steam:1455840 | Dorfromantik | 2.5D但拓扑平面；Steam | 逐块放置/旋转多边地形，邻接拼合得分，扩大图景 | 六边或四边拼块对齐邻接，延续自造局面 | 类Carcassonne / Domino Grove已成熟，不能只简化而得优势；任务和美感共同贡献 | PARK / COMMODITY_OVERLAP | https://store.steampowered.com/app/1455840/Dorfromantik/ |
| steam:977950 | A Dance of Fire and Ice | 2D；Steam | 单按键按节拍前进，路径形状提前提示节奏 | 一条折线/几何路径与固定节拍的同步按点 | 不同歌曲谱面、音频校准和手感决定乐趣；不等于随意点几下 | PARK / AUDIO_CONTENT_COST | https://store.steampowered.com/app/977950/ADanceofFireandIce/ |
| steam:1404850 | Luck be a Landlord | 2D；Steam | 每轮转动产生得分，符号增益及道具协同形成成长构筑 | 小量符号下的简单相邻倍增/结算 | 官方强调大量符号与道具多样性，缩到6种很可能无深度、同类老虎机玩法多 | SKIP / SYSTEM_CONTENT_COST | https://store.steampowered.com/app/1404850/Luck_be_a_Landlord/ |
| steam:1948280 | Stacklands | 2D；Steam | 将卡牌堆叠以转化物品、维持生存与经营 | 两三个对象的拖拽合成/产出 | 原作有200+卡牌、60+创意、50+任务及经济循环，削减后只是固定配方合成 | SKIP / SYSTEM_CONTENT_COST | https://store.steampowered.com/app/1948280/ |
| steam:1296610 | Peglin | 2D；Steam | 发射球撞钉累积伤害，特殊球与遗物放大回报 | 极简弹射撞击→触发链 | 已有 Bounce Lab，物理与目标系统重复；删升级后可能无持续成长；独立同类多 | PARK / PORTFOLIO_DUPLICATE | https://store.steampowered.com/app/1296610/peglin/ |
| steam:923260 | Golf Peaks | 2D/2.5D；Steam | 通过有限动作卡选择方向和位移解谜 | 球+几张步数/方向卡+有限棋盘 | 官方有120+手工关卡，长线题库成本高，取掉动作卡后类似一般推箱逻辑 | SKIP / MANUAL_LEVEL_COST | https://store.steampowered.com/app/923260/Golf_Peaks/ |
| steam:915310 | SNKRX | 2D；Steam | 维持蛇形运动，自动攻击，英雄职业搭配成长 | 转向控制 + 位置决定触发的简化跟随攻击 | 官方有40+英雄、12+职业、40+被动、25+关卡；保留操作易、保留兴奋难 | SKIP / SYSTEM_CONTENT_COST | https://store.steampowered.com/app/915310/SNKRX/ |
| steam:1794680 | Vampire Survivors | 2D；Steam | 自动攻击、在生存压力中走位、收集经验不断成长 | 几何角色走位躲敌自动击中 | 主要长期动力是武器演化、解锁、成长曲线与大量内容；原作/大量复制品竞争强 | SKIP / SYSTEM_CONTENT_AND_COMPETITION | https://store.steampowered.com/app/1794680/Vampire_Survivors/ |
| steam:1291340 | Townscaper | 3D例外；Steam | 点一下方块，美观建筑依邻接自动生长，提供创作惊喜 | 邻接几何块在二维下变成自组织图案 | 原作官方强调没有目标、主要是美丽的程序化建筑。删3D景观和生成资产等于删掉快乐 | SKIP / UX_TRANSFER_LOSS | https://store.steampowered.com/app/1291340/Townscaper/ |

备注：名单中的 Sandtrix 已有可玩的原始极简版本，我们的研究机制是“离散放置→连续形态变化”，**不能直接复刻 Sandtrix**；Wilmot、Digging 均不能假定去掉内容后仍有快乐；Dorfromantik 在 Steam 标签中含 3D，但决策拓扑属于可平面化排列，归入 2.5D 源，而非额外占3D例外。

## 最值得新增研究的三个机制 DNA
1. **可变形空间约束**（优先 WATCH）：一次放置后静态拼块变为多点连续状态，使同一位置有不可预料但可理解的次生效果。并不是默认复制横向同色消除。NEXT：在纯规则纸面确定一种与现有沙块拼图实质不同的“可学习取舍”，再决定是否实现64×64简化落沙。KILL：小规模只剩随机落沙，策略差异难区分；高度近似现成 Sandtrix。
2. **自己构造的信息组织→随后需要重新访问**（优先 WATCH）：玩家按照自己创造的分类布局组织对象，后续系统以不可预知但透明的请求检验布局。NEXT：12个符号无美术真人静态试验，区分“整理有满足感”和“被考记忆”两种体验。KILL：人们普遍不自发整理、只依赖死记、5轮无自发续玩。
3. **挖掘→局部揭示→下一目标自然浮现**（条件备选）：保留2D空间揭示，先不用升级系统。NEXT：纸面画3层不同分布的隐藏材料，检查是否自然产生路径选择；若不依赖升级和秘密宝箱依然无乐趣，停。KILL：必须大量图案/剧情、数值升级才吸引。

## 强反例、框架避免误用
- 本轮没有任何新方向是已证原创。Wilmot的整理回收、落沙和2D挖矿都存在相邻乃至直接产品。需要后续查重+明确表达差异。
- 2D容易做不是“轻量可运营”；尤其 SNKRX/Vampire Survivors/Stacklands，最核心乐趣可能就是规模内容和组合平衡。
- 纯数字/符号的整理游戏可能不再有 Wilmot 的语义分组，这正好是反向提纯失败的正例。
- 对 Sandtrix 原作已经完成极简版本，再做“更少美术”会变成更差的拷贝；只有发现不同的玩家行为才升级。
- 三条都尚无零解释试玩、策略模拟、竞品差异或真实留存。现在只是 RULE_PROBE/PARK。

## Decision Log
Decision：12样本完成官方来源文献筛选，前2 RULE_PROBE，第3 CONDITIONAL，其余 PARK/SKIP；没有直接立项。
Supporting Evidence（FACT）：官方游戏介绍列出的操作及内容规模；反证为明确的大型关卡/资产/玩法系统需求。
INFERENCE：提纯后核心快乐能否被保留、实现工作量与视觉读图成本。
Unknown：首玩理解、5局复玩、移动端真实手感、差异化和用户渠道。
Kill：原作深度依赖重内容、美术/音乐、复杂实现；即使删去这些后仍没有可学习的局面/动作变化。
Next Evidence：先做研究级规则草图或纸面测试，确认不同于源作的独立核心机制，再决定何时进行1–3天原型。
Registry：research/game-registry/GAMES.tsv（main跨分支统一去重）；后续扫描开头必须读主分支最新索引，不能只靠聊天记忆。

