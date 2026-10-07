# Codex Task — Chain Shot HTML Prototype V0.1

你正在实现一个一次性核心玩法验证，不是在制作完整游戏。

## Mission

做一个无需构建工具、双击即可运行的单文件 HTML：

`prototype/chain-shot-v0.1.html`

目标是在桌面和手机浏览器中验证：

**点击一个 Seed → 箭头连锁分叉 → 玩家理解结果 → 想换 Seed 重试。**

## Hard Scope

只允许：
- HTML
- CSS
- Vanilla JavaScript
- Canvas 2D
- WebAudio 可选

禁止引入 npm、框架、图片、字体、后端、联网、存档和第三方库。

## Exact Rules

- 7×9 grid
- node = {x, y, dir}
- 8 directions only
- one manual tap per attempt
- activated node fires a pulse
- pulse travels cell by cell until outside board
- pulse DOES NOT stop after hitting a node
- every unactivated node crossed by pulse activates and emits its own pulse
- node activates once
- when no pulses remain:
  - all nodes active => success
  - otherwise => fail

## Architecture

Keep it small:

```
LEVELS
state
resize()
resetLevel()
activateNode(index)
spawnPulse(node)
stepSimulation()
update(dt)
draw()
handlePointer()
playTone()
```

不要建立 GameObject/Entity/System 类层级。

## Rendering

Canvas should:
- fit portrait mobile;
- cap playable width around 520px;
- keep node hit targets >= 44 CSS px where possible;
- render crisp at devicePixelRatio;
- draw grid subtly;
- draw arrow glyph or geometric arrow;
- visually distinguish dormant vs activated nodes;
- draw moving pulse heads and short trails;
- show activated / total.

## Interaction

Top UI:
- Level
- Activated / Total

Bottom UI:
- Restart
- Demo
- Next only after success

On board:
- tapping a node when idle starts the only manual action;
- ignore additional board taps while cascade is running.

Demo button:
- reset current level;
- automatically tap the predefined solution Seed after a short delay.
- This exists so the prototype can be screen-recorded as a short demo.

## Feedback

Add only lightweight juice:
- activation scale pop / expanding ring;
- small particles;
- synthesized short tone;
- slightly increasing pitch with combo;
- subtle screen shake on larger cascades.

Feedback MUST NOT change collision/simulation behavior.

## Level Data

Use five curated levels; store solution index only for Demo. Do not expose answer during normal play.

Suggested data:

```js
[
  {
    solution: 2,
    nodes: [
      {x:4,y:2,dir:"DL"},
      {x:4,y:6,dir:"U"},
      {x:5,y:6,dir:"L"},
      {x:4,y:3,dir:"R"},
      {x:2,y:6,dir:"DR"}
    ]
  },
  {
    solution: 0,
    nodes: [
      {x:5,y:3,dir:"D"},
      {x:5,y:4,dir:"UL"},
      {x:6,y:6,dir:"U"},
      {x:6,y:5,dir:"L"},
      {x:5,y:6,dir:"R"},
      {x:6,y:0,dir:"DL"},
      {x:4,y:5,dir:"DL"}
    ]
  },
  {
    solution: 7,
    nodes: [
      {x:1,y:1,dir:"R"},
      {x:2,y:1,dir:"DR"},
      {x:6,y:0,dir:"L"},
      {x:0,y:0,dir:"U"},
      {x:3,y:0,dir:"U"},
      {x:1,y:8,dir:"UL"},
      {x:3,y:1,dir:"DR"},
      {x:3,y:3,dir:"UR"},
      {x:1,y:0,dir:"D"}
    ]
  },
  {
    solution: 4,
    nodes: [
      {x:3,y:6,dir:"U"},
      {x:0,y:4,dir:"UR"},
      {x:6,y:8,dir:"UL"},
      {x:2,y:2,dir:"DR"},
      {x:5,y:4,dir:"UR"},
      {x:3,y:1,dir:"DL"},
      {x:3,y:5,dir:"DR"},
      {x:3,y:3,dir:"D"},
      {x:4,y:5,dir:"U"},
      {x:3,y:7,dir:"D"},
      {x:6,y:3,dir:"DL"}
    ]
  },
  {
    solution: 1,
    nodes: [
      {x:6,y:1,dir:"DL"},
      {x:0,y:0,dir:"D"},
      {x:0,y:6,dir:"D"},
      {x:0,y:7,dir:"R"},
      {x:5,y:5,dir:"UR"},
      {x:0,y:4,dir:"UR"},
      {x:0,y:5,dir:"R"},
      {x:6,y:7,dir:"U"},
      {x:0,y:1,dir:"DL"},
      {x:1,y:7,dir:"DL"},
      {x:5,y:7,dir:"D"},
      {x:2,y:5,dir:"UL"},
      {x:6,y:4,dir:"UR"}
    ]
  }
]
```

## Acceptance Checklist

- [ ] Double-click HTML works with no server.
- [ ] Resize works.
- [ ] Pointer/touch works.
- [ ] One tap can spawn multiple simultaneous branches.
- [ ] Rays pass through hit nodes.
- [ ] A node never fires twice.
- [ ] Result waits until every pulse has left board.
- [ ] Restart is instant.
- [ ] Demo can auto-play a successful cascade.
- [ ] No console errors.
- [ ] No framework or external asset.
- [ ] Code stays readable enough to delete/rewrite quickly.

## Do Not “Improve” Yet

Do not add:
- obstacles
- enemies
- special arrows
- score economy
- powerups
- procedural level generation
- skins
- progression
- tutorial system

If the core loop is weak, those additions are not fixes.
