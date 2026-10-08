# Chain Shot FX Lab — 2026-10-08

## 运行与范围

双击 `prototype/chain-shot-fx-lab.html`，四个音频素材已内嵌，无网络、服务器或手工上传依赖。先选素材，再选单次/12连击，切换Classic+Pop或Balloon Blast重播。可对比纯Pop、Pop+低频、Pop+V0.3双层Hit，以及只听V0.3 Hit。

没有修改V0.3、十关数据、Solver或README。页面仅做固定试听与原第6/10关同Seed回放，没有新规则、编辑器或游戏进度系统。

## 实际素材与授权

已下载并核实CC0；原文件哈希与实际下载URL在 `prototype/fx-lab-assets/sources.json`。

|候选|来源|实际取得的文件|
|---|---|---|
|Lukeo135 Balloon Pop|https://freesound.org/people/Lukeo135/sounds/563197/|公开HQ MP3预览；原始WAV需登录，未下载原WAV|
|Breviceps Balloon Pop|https://freesound.org/people/Breviceps/sounds/458398/|公开HQ MP3预览；未下载原WAV|
|Kenney Generic Light|https://kenney.nl/assets/impact-sounds|官方ZIP内 impactGeneric_light_000.ogg|
|Kenney Pluck|https://kenney.nl/assets/interface-sounds|官方ZIP内 pluck_001.ogg|

Freesound页面实际包含CC0 1.0链接，相关HTML片段保留；Kenney官方包的原License.txt保留。CC0允许复制、修改及商业使用。没有提取Peggle/泡泡游戏音频，也未将预览冒称无损原音。候选依据来源、瞬态时长、正常解码和输出幅度筛选；尚未主观试听，未认定某个音效已经最好听，也未将Kenney Pluck称为真实泡泡录音。

## 固定实验参数

所有候选自动去除前导静音（原峰值12%阈值前留1ms）、按原峰值归一0.7、最多140ms、尾部8ms淡出。12击固定120ms间隔，无随机升调；这是峰值匹配，**不是LUFS响度匹配**。主增益0.55，压缩器阈值-12dB、比例12、attack 2ms、release 80ms；它不是保证任意输入永不削波的brick-wall limiter。

Pop先安排播放，低频与V0.3合成Hit使用独立最多3个可选声部；同刻多节点合并为一个Pop重音，不丢失视觉节点事件。当前固定测试时间线最多2个同时Pop，总声部受已知时间线与可选层限额约束；不提供任意高频事件输入。V0.3 Hit复用原三角波主体+正弦高频层。

Classic保留徽章；Blast在命中时间点即刻替换实体为淡圈和原方向箭头，不使用实体渐隐。45ms预压缩、16ms白闪、140ms冲击环/非对称实心碎片。两模式完全共用同一时间线。第6/10关回放用原格位、方向、Seed和88ms等待/cell-step，确定性记录事件，不更改主游戏模拟。新增父子传播短轨迹帮助追踪命中因果。

音频提前80ms安排，动画使用AudioContext输出时间戳；没有用独立setTimeout启动音频。第一帧显示仍受刷新率限制，不宣称物理设备零毫秒偏差。

## 已执行测试

`python tools/test-fx-lab.py`：Windows Edge/CDP，测试主机使用websocket-client（游戏没有依赖）。结果和截图在 `tools/fx-lab-test-artifacts/`。

- 四个文件实际解码，准备后的时长99.5–140ms。
- 4素材 × 2动画 × 单次/12击/第6关/第10关 = 32组合，事件数分别1/12/12/18；Pop组安排成功，可选层上限通过。
- 原第6/10关的全部激活时间与独立Python cell-step记录逐项一致，两动画不改变时间线。
- 实际播放完整12次，记录每次首个视觉命中帧相对输出时钟的偏差；明细在results.json。
- 四候选经相同总增益/压缩参数OfflineAudioContext渲染12连击：峰值约0.574–0.606，全部有限，无数字削波。该测试不代表耳朵已听过。
- 1000×900、390×844、320×568视口无横向溢出；页面允许纵向滚动。
- 静音总增益0、停止清空、选项更换取消旧播放；控制台异常0，无外部资源请求。
- 截图已观察移动页面与爆裂后方向残影。稳定V0.3、关卡和Solver无diff。

## 仍需人工体验

请用耳机和手机扬声器比较四候选：单次是否够干脆、12击是否刺耳/像机关枪、加低频是否掩盖瞬态、Blast残影是否足够帮助复盘。峰值匹配不能保证感知响度公平；如果某个明显更响，应在听感评审时指出，下一轮再做有依据的响度调整。

真实手机音频解锁、蓝牙延迟、后台返回及低端机帧稳定性未验收。本站试听已做出可比较结果，但不代替真人听感结论。Classic仍为默认，没有预判Blast胜出。
