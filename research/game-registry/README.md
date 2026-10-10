# Game Scan Registry V0.1 — 游戏扫描去重登记簿

日期：2026-10-09。**GitHub main 分支是跨对话/跨研究分支的游戏扫描登记唯一入口**：
[GAMES.tsv](GAMES.tsv)。
最初收录 **36 条**（12 个新增样本 + 24 个历史参考）；2026-10-09 已扩至 **42 条**，2026-10-10 经 Route B 定向轻度益智扫描已扩至 **54 条**；同日完成乐趣优先 V4.0 后增至 **66 条**，后续以 GAMES.tsv 的实际行数为准。
注意：早前用户提供的 50 款截图样本库尚未逐条完整匹配 canonical ID，因此**不应声称此前 50 款已全量去重**；后续补档应按来源逐步添加。

## 为什么用 TSV
一行=一个**具体源游戏**，不是一个 idea、一种机制或一个店铺搜索词。表格可由 GitHub 直接 diff/检索，也可导入 Excel/Sheets，规模变大再考虑生成脚本；现在不引入数据库、爬虫或复杂状态机。禁止同一 canonical key 出现两行。

字段：
- game_id：优先稳定 ID，如 steam:2546310、play:com.gamebrain.hexasort；否则平台/作者/slug，例如 itch:msky-dev/sandtrix、poki:level-devil。缺失时临时 name:规范英文名，发现商店稳定 ID 后迁移 canonical ID 并保留旧别名。
- title：原作规范名。
- aliases：其他平台/版本/中文或英文常用别名，英文小写用分号分隔。**别名不等于已核实的完全同一游戏版本**，遇到同系列不同版本应确认是否要拆行。
- source_type：2D、2.5D、3D例外与来源平台等最简提示。
- status：当前实验室研究处置结果，**不代表游戏质量或市场前景**。
- reason_code：为什么不继续或存在何种关键阻碍；不要写“无聊/不好玩”冒充人测结论。
- recheck_trigger：以后什么时候才允许重新扫描；没有触发不重复做长评。
- source_url：官方商店或开发者原站；可点击核验，勿杜撰链接。
- evidence_report：研究报告位置简称。
- last_checked：这个“已评估”的日期，不是游戏上线日期、行情或数据更新日期。

## 状态解释和重复扫描政策
- **PROBE**：值得做最小规则/纸面/人测试验。下一次要推进证据而不是重新搜索同一游戏。
- **CONDITIONAL**：只保留条件性备选，先解决指定根本风险，不纳入常规开发队列。
- **PARK**：有可迁移元素但目前不优先，如同质化、与现有实验室项目重叠；只做轻量来源保存。
- **SKIP**：当前 Solo Fit / 内容成本 / 表达迁移 /市场 Gate 未通过。本轮显式淘汰；默认下轮不再深扫，除非满足 recheck_trigger。
- **REFERENCE**：之前已经研究过，作为比较基准；**不应自动当成不合适或已测试失败**。避免旧例反复长篇分析。
- 如确有新证据，可更新该行 status 与 reason 并在新的研究报告留出 Decision Log；不要直接删除旧行。

常用原因：
SYSTEM_CONTENT_COST（道具职业/配方内容太多）；MANUAL_LEVEL_COST（大量手工关卡）；UX_TRANSFER_LOSS（核心愉悦随简化载体丢失）；AUDIO_LEVEL_CONTENT（音乐与谱面）；PORTFOLIO_DUPLICATE（与现有实验重复）；SIMILAR_MARKET（成熟同质化）；REPRESENTATION_RISK（用简单符号无法自然表达）；MECHANIC_DIFF_UNVERIFIED（尚未找到与原作有意义的机制差异）；REVEAL_CONTENT_RISK（快感依赖不断准备惊喜内容）；PREVIOUS_SCAN（前轮已研究的基准）。

注意：Sandtrix 的 Sandtris/Setris 通用称呼可能与其他厂商独立作品重名。**不可按近似标题自动合并**，必须先用开发商和商店稳定 ID 辨别具体产品；不同开发商的 SandTris™ 独立登记。

## 下轮扫描的最短工作流
1. 开始前读取 main 的 GAMES.tsv。对新候选先查商店游戏 ID / 正规 URL，再查 title / aliases；同款改名、跨平台移植要人工识别。**查重在深度拆解之前**。
2. 若已在表中，先看 status：SKIP/REFERENCE/PARK 通常不再深扫；PROBE 继续验证；CONDITIONAL 只在触发条件满足后重审。
3. 确实新游戏，才做 Route B 三 Gate：行为快乐可搬运 → 视觉与动作自然一致 → Solo 原型/体验/内容成本。
4. 无论结果，保存一行；即使不符合条件，也写出具体 reason_code、源出处和下一次恢复研究的触发条件。
5. 批次结束时，每 12 新样本原则上只留 2-3 核心机制进一步验证；研究报告保存在研究分支，通用成熟结论再合并 main。
6. 不把抽象机制 DNA 登记为具体游戏。相同机制来自不同游戏时，游戏 ID 可以多行，但在报告中指向同一父机制并标注已有先例，防止 Idea 层重复。

## 本轮引用来源（不是长期“版本号”）
- **scan-v2** → [GLOBAL_DISTILLATION_V2.0_12.md](https://github.com/ChengK321/Kai-Game-Design/blob/research/global-mechanic-scan-20261009/research/global-mechanic-scan/GLOBAL_DISTILLATION_V2.0_12.md)
- **scan-v1** → [GLOBAL_SCAN_V1.0.md](https://github.com/ChengK321/Kai-Game-Design/blob/research/global-mechanic-scan-20261009/research/global-mechanic-scan/GLOBAL_SCAN_V1.0.md)
- **previous-reference** → [MECHANIC_DISTILLATION_V0.1.md](https://github.com/ChengK321/Kai-Game-Design/blob/research/global-mechanic-scan-20261009/research/global-mechanic-scan/MECHANIC_DISTILLATION_V0.1.md) 与 [ROUTE_B_SOLO_FIT_V0.2.md](https://github.com/ChengK321/Kai-Game-Design/blob/research/global-mechanic-scan-20261009/research/global-mechanic-scan/ROUTE_B_SOLO_FIT_V0.2.md)

## 文件扩容原则
数百项仍可用 TSV + 搜索；若接近几千条再考虑拆按 canonical ID 前缀建立分表，并保留自动生成的统一索引。没有真实查重瓶颈前，不开发新系统。

### Route B V3 定向扫描（2026-10-10）
本批 12 款依据已确认的“极简规则驱动休闲益智 / 忠实提纯而非强制原创”标准研究；
[12 款详细评审](https://github.com/ChengK321/Kai-Game-Design/blob/research/minimal-puzzle-scan-v3-20261010/research/minimal-puzzle-scan/ROUTE_B_TARGETED_SCAN_V3.0.md)。
本轮 PROBE 表示准许做小原型验证，并不等于得到实际人类游玩或市场正反馈。KAMI 2 的出题质量必须先经独立 Gate。

### V4.0 乐趣优先机制扫描（2026-10-10）
新增 12 款跨网页/移动端/实体牌面机制源，首次把“愿不愿主动操作下一步”置于 Solo Fit 之前；其中 2 个 RULE_PROBE（Flood-It 和 SET），1 个 CONDITIONAL（Infinity Loop），其余全部保留具体参照、暂缓或淘汰原因。
[完整报告与策略仿真](https://github.com/ChengK321/Kai-Game-Design/blob/research/pleasure-first-scan-20261010/research/pleasure-first-scan/PLEASURE_FIRST_SCAN_V4.0.md)。
不能把 PROBE 当成玩家留存已验证，也不能把 REFERERENCE/PARK/SKIP 当成原作市场失败。
