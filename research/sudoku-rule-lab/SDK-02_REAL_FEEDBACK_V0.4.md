# SDK-02 交点亮灯：外部静态试玩反馈与去留判断 V0.4

Date: 2026-10-09
Status: WATCH / DEPRIORITIZED (not KILLED). No game code requested.
Context: prior visual-gate V0.3 includes 4-socket intro and 7-socket organic/regular cards.

## 真实反馈（用户提供聊天截图，非正式、非引导盲测）
- 测试者看第二张图“没太看懂”，问能否加箭头；
- 问“点亮的顺序”；
- 问“线上的一二三数字”是什么意思；
- 也评价“感觉还挺有意思”。

User explains: no arrow; no order; each colored line exactly one lit light; numbers are line labels and seemingly redundant.

FACT: 这个参与者把线路联想到有方向、有点亮先后次序的实体连线，并把编号当潜在线索。
INFERENCE: 表达载体不是规则天然的可视化；编号虽为设计辅助，却额外引入认知疑问。
UNKNOWN: 其他完全陌生玩家的表现、题目是否有独立吸引力、同一机制换别的可视形式是否改善、读图困难来自画面尺寸还是语义本身。
COUNTER EVIDENCE: 玩家也觉得有意思；单次朋友聊天 + 截图尺寸/测试方法不严格，不能证明游戏必败。
RISK: 规则解释依赖沟通者反复澄清“没有方向/没有顺序”，违背无教学上手目标；更多配色、数字或箭头可能改变/扩大规则而不是解决问题。

## 新的跨游戏类比
《一箭又一箭》2026 开发者大会回顾：加目标颜色和缓冲区的融合尝试降低纯粹体验，后来保留简单箭头清除的主乐趣，低频新机制、更多关注关卡供给与难度节奏。
Primary developer talk reprinted: https://news.yxrb.net/2026/0528/7007.html

## Decision
- Pause SDK-02 作为正式玩法候选，不进入交互 Prototype，也不额外制作更多线路优化版或 UI 系统。
- 机制基因「重叠约束 → 必然推理 → 逐步确定」仍保留在 Rule Atlas。
- 对比 Sudoku / Queens / Arrow Out 的关键是表示与规则的天然一致性，不能只优化出题数学。
- If revived, require a fundamentally clear, no-translation visualization within 1 simple silent test, not incremental numbering/hints; then test repeat value.

## Next evidence and kill
Present only existing diagrams to 3-5 complete strangers on phone without explanation; ask them to point to a legal first choice and say why, log misunderstandings. No new rules. If confused about path membership/direction/sequence persists, mark *交点亮灯这一形式* KILLED; do not kill its parent mathematical mechanism.
