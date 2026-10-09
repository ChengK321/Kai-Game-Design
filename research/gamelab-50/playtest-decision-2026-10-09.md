# One-Rule Lab｜首次比较试玩复盘（2026-10-09）
性质：小规模、非结构化用户反馈；不是随机对照试验、下载量或留存数据。

## 当前决定
- **Endless Peel V0.4：继续探索**。端点补块预告后主观体验比 V0.3 明显改善；核心试玩者主动多局、平均约20回合、最好80和次好70（自述，缺seed和逐局记录）；连续大剥离被直接描述为“有乐趣”。不立刻改规则或降低难度。
- **Ring Shift V0.1：暂停**。试玩者明显感到烧脑和“压力大于乐趣”，输入选择多/直接收益不明显可能是根因，不能以“还没找到技巧”作为自动继续理由。
- **不应把正向试玩直接升级为爆款证据**。Next Gate：不参与研发的5–8位试玩者、真实每局记录、复玩意愿和同种子对照。

## 最小问题复核
- 已核实的 Peel V0.4 源码显示：`makeGhost` 的风险橙色提示只按当前行长度＋未来补块数判断，**没有考虑本次实际剥离**，因而只能表示潜在压力，不能作为所选操作必死判断。先解决提示准确性，避免人为增加焦虑。
- 唯一拟议的后续参数对照：相同颜色数量、补块量、起始生成规则，容量9 vs 10；以9为对照。不能同时改补块/颜色/容量以免失去归因。
- 观察最强快乐事件「跨多排连续剥离」，但不因该事件好玩就马上叠加连击技能、特殊方块和复杂声光反馈。

## Evidence Labels
- FACT (self report)：上述试玩经历和回合数自述。
- FACT (code)：两个原型的当前运行规则以及静态告警条件。
- INFERENCE：Ring Shift 16种行动的搜索成本可能大于即时快乐；Peel 连续剥离构成有效体验钩子。
- HYPOTHESIS：更可信的临危预警和局末死亡回放可能进一步改善公平感；尚未真人验证。
- UNKNOWN：真实新手前10秒理解率、复玩概率、20与80回合差异的技能/随机原因、哪套难度更好。

## 分支出处
- [Peel 试玩记录](https://github.com/ChengK321/Kai-Game-Design/blob/concept/peel-peel/concepts/peel-peel/PLAYTEST_V0.4_FEEDBACK.md)
- [Ring Shift 试玩记录](https://github.com/ChengK321/Kai-Game-Design/blob/concept/ring-shift/concepts/ring-shift/PLAYTEST_V0.1_FEEDBACK.md)
