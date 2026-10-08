# Chain Shot V0.3.1 — 游戏内 FX 实现与测试

## 如何比较

双击 `prototype/chain-shot-v0.3.1.html`。默认第6关、Classic、方向族配色、Lukeo135 Pop（暂定候选，不代表玩家已选定赢家）。关卡下拉可直接进入全部十关，建议先试6和10。

选择任意箭头启动真实连锁。用“同 Seed 重播”保持选择不变，切换命中音效/Classic与Balloon Blast后重播。切换会停止并重置当前局，保留同Seed；换关清除Seed。重来允许重新选择起点，下一关仍只在成功后可用。总音量、静音在对照切换中保留。

`?level=10&audio=synth&mode=classic` 可指定入口；`?debug=1` 提供Demo与索引，正常入口不显示答案。

## 改动与素材

只新增V0.3.1 HTML、局部构建脚本、浏览器验证工具、测试证据及本报告。V0.3、FX Lab、原十关JSON、Solver、来源素材和README均未修改。

HTML内嵌复用FX Lab的四个授权录音及其来源/校验信息，file://无需fetch或网络：

- Lukeo135 Balloon Pop：https://freesound.org/people/Lukeo135/sounds/563197/
- Breviceps Balloon Pop：https://freesound.org/people/Breviceps/sounds/458398/
- Kenney impactGeneric_light_000.ogg：https://kenney.nl/assets/impact-sounds
- Kenney pluck_001.ogg：https://kenney.nl/assets/interface-sounds

均复用此前实际下载并记录的CC0素材；Freesound是公开HQ MP3预览，未冒称原始WAV。原授权与SHA256在 `prototype/fx-lab-assets/`，本轮没有新增下载或引入受保护游戏音频。

## 实现要点

- 实际 `activateNode` 收集命中；每个实时cell-step结束后安排本tick的声音。同tick多个命中合并为一个Pop重音，每个节点的激活和视觉反馈仍独立。没有录制时间线，没有为了音频节拍修改游戏判定。
- 四音色 × 两视觉共享原cell-step遍历、等待88ms、穿透、分叉、单次激活、所有Pulse离场才结算。所有十关格位/方向/Seed与原JSON一致。
- 合成对照保留原双层Hit（triangle主体+sine高频）及公共启动/结算；音效不随视觉开关改变。Pop替代命中层，避免再叠加合成Hit、Explosion、Travel或Branch形成混音偏差。
- Pop有独立最多4声部，合成层不能抢占；溢出时替换最旧Pop。当前实际十关的140ms短样本通常最多两组重叠。自然瞬态保留，尾部8ms处理；倍率按固定序列1/.99/1.015/.985微变，不无限升调，同Seed重试重置序列。
- 自动去前导静音，最大140ms；按RMS目标0.008调整，同时以原峰值0.65限制增益，避免单纯把Pop放大。此为粗略能量控制，**没有LUFS或感知响度匹配**，瞬态与持续音色仍可能听起来不一样响。主增益默认0.65，提供0–1滑块；沿用原压缩器，不声称是brick-wall limiter。
- 页面加载先解码；首次玩家手势恢复AudioContext。首局如尚未解码，会显示“音频准备中”再开始，期间只接受一个Seed。异步启动有attempt令牌；重试/切换/停止或隐藏页面会取消旧启动、停止全部旧音源，避免晚到的声音。静音立即归零增益并停止音源。
- Classic点亮表现保留。Balloon Blast在真实命中瞬间换成淡圈和原方向箭头，Seed在实际释放时破裂；16ms白闪，140ms冲击环和少量实心方向碎片，没有缓慢实体淡出。逻辑节点一直保留，后续Pulse可以穿过原位置。

## 实际执行测试

`python tools/test-v031-browser.py` 使用Windows Edge/CDP；测试主机依赖websocket-client，游戏无需依赖。结果与截图保存在 `tools/v031-test-artifacts/`。

- 全110个Seed × 5音效选择（原合成+四Pop）× 2视觉 = **1,100次**，全部与独立Python Solver最终集合一致。含核心2×2的440次；所有正解可通关。
- 连锁中第二Seed被拒绝；每步无提前结算；200步以内全部结束；重试清空节点、Pulse、声音、命中记录；启动后立即重试不产生晚到局。
- 第6关真实CDP触摸正确Seed6（索引从0开始）全清12节点；近失误Seed0实际10/12并失败。截图检查未触发实体与原方向残影可区别。
- 第6关切换原合成/Classic后同Seed重播正常；第10关真实触摸与同Seed重播全清18节点；中途静音即时停止声部，恢复后继续正常。
- 第10关实际产生的命中日志18个不同节点，Pop组计数合计18。每组声音开始与实际激活记录相差小于20ms，通常同一tick内；不是预先录制时间表。
- 将实际第10关的Pop时间、分组和倍率离线重渲染四素材：峰值约0.027–0.107，全部有限、无数字削波。此测试覆盖Pop总线，不等同整机扬声器试听。
- 1000×900、390×844、320×568视口无横向溢出。短屏纵向滚动，760px最小内容高度避免节点和按钮挤在一起；高DPI渲染倍率最多2。
- Runtime异常与控制台error为0；无HTTP/HTTPS请求；V0.3、FX Lab、十关和Solver无diff。

## 尚未验收与人工Gate

未实际试听桌面耳机/手机扬声器，不能凭无削波认定更好听。真实手机音频权限、蓝牙/硬件延迟、前后台恢复和低端机帧稳定性待确认。声音在实际命中帧安排，但显示刷新与音频输出延迟意味着不保证物理零延迟。

建议固定第6关同Seed比较原音效/Pop，再固定Pop比较Classic/Blast；重试一个错误Seed，最后比较第10关密集连锁：Pop像物理接触还是UI点击？是否刺耳/像机关枪？Classic+Pop是否已经满足？Blast事后能否看清原方向和漏点？是否想重新选Seed而不只是回放？

Classic仍默认。没有预判Blast胜出，也未修改关卡或处理失败信息泄露问题。

## Git

实现提交：`7add17c469eb48e0344d08f5ad0fbcc63efa5ac8`。已成功推送至 `origin/design/chain-shot-v0.1`（远端从 `c6f5dcb` 更新至 `7add17c`）。本段是随后补充的交付记录；没有合并main。
