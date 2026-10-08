# coding: utf-8
import pathlib,re,json
root=pathlib.Path('.');h=(root/'prototype/chain-shot-v0.3.html').read_text(encoding='utf8')
lab=(root/'prototype/chain-shot-fx-lab.html').read_text(encoding='utf8');assets=json.loads(re.search(r'const ASSETS=(\[.*?\]),BOARDS=',lab,re.S)[1])
h=h.replace('V0.3','V0.3.1').replace("params.get('theme'):'minimal'","params.get('theme'):'direction'")
h=h.replace('min-height:720px','min-height:760px').replace('top=210,bottom=148','top=250,bottom=148')
h=h.replace('<label class="theme">配色 <select id="themeSelect">','<label class="theme" hidden>配色 <select id="themeSelect">')
h=h.replace('<button id="muteBtn"', '''<label class="audio-choice">命中 <select id="audioSelect"><option value="synth">原合成 Hit</option><option value="balloon">Pop · Lukeo135</option><option value="balloon2">Pop · Breviceps</option><option value="impact">Pop · Kenney Impact</option><option value="pluck">Pop · Kenney Pluck</option></select></label>
  <div class="compare-row"><label>关卡 <select id="levelSelect"></select></label><label>音量 <input id="volume" type="range" min="0" max="1" step="0.05" value="0.65" aria-label="总音量"></label></div>
  <button id="muteBtn"''')
h=h.replace('<button id="nextBtn"','<button id="replayBtn" disabled>同 Seed 重播</button><button id="nextBtn"')
h=h.replace('</style>','''
    .audio-choice {position:absolute;top:130px;left:18px;z-index:6;display:flex;align-items:center;gap:6px;font-size:12px;color:#65716a}
    .audio-choice select {max-width:195px}
    .compare-row {position:absolute;left:18px;right:18px;top:182px;z-index:6;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:12px;color:#65716a}
    .compare-row label {display:flex;align-items:center;gap:6px;min-width:0}
    #levelSelect {max-width:180px} #volume {width:90px;accent-color:#408667;min-height:44px}
    .controls {grid-template-columns:1fr 1.2fr 1fr}.controls.debug {grid-template-columns:1fr 1fr 1.2fr 1fr}
    [hidden] {display:none!important} #debugInfo {top:230px}
    @media(max-width:340px){.audio-choice select{max-width:170px}#levelSelect{max-width:145px}#volume{width:60px}.controls{gap:5px}.controls button{font-size:12px}}
  </style>''')
pos=h.index('const params=');h=h[:pos]+'const POP_ASSETS='+json.dumps(assets,ensure_ascii=False)+';\n'+h[pos:]
h=h.replace("let cssW=", "let audioMode=params.get('audio')==='synth'?'synth':(['balloon','balloon2','impact','pluck'].includes(params.get('audio'))?params.get('audio'):'balloon'),volume=.65,lastSeed=null,starting=false,attemptId=0,popReady=null,popBuffers={},impactBatch=[],hitLog=[],popLog=[],popCounter=0;const liveSounds=new Set();\nlet cssW=")
h=h.replace('currentLevel=0,nodes=',"currentLevel=Math.max(0,Math.min(9,(Number(params.get('level'))||6)-1)),nodes=")
h=h.replace('function resetLevel(){clearTimeout', 'function resetLevel(){attemptId++;starting=false;stopSounds();impactBatch=[];hitLog=[];popLog=[];popCounter=0;clearTimeout')
h=h.replace('nextBtn.disabled=result!=="success";', 'nextBtn.disabled=result!=="success";document.getElementById("replayBtn").disabled=lastSeed===null;document.getElementById("levelSelect").value=currentLevel;')
h=h.replace('master.gain.value=muted?0:.65','master.gain.value=muted?0:volume')
h=h.replace("function ensureAudio(){", "function ensureAudio(resume=true){")
h=h.replace("if(audioCtx.state==='suspended')return", "if(resume&&audioCtx.state==='suspended')return")
# Audio function gets lifecycle tracking and independent pop pool.
h=h.replace("if(!audioCtx||muted||audioCtx.state!=='running')return;const scale", "if(!audioCtx||muted||audioCtx.state!=='running')return;if(audioMode!=='synth'&&['hit','explosion','branch','travel'].includes(event))return;const scale")
h=h.replace('voices++;const now=', 'const now=')
h=h.replace("source.start(now);source.stop(now+duration+.01);source.onended=()=>{voices--;source.disconnect();if(filter)filter.disconnect();gain.disconnect()}", "const entry={source,gain,kind:'synth'};liveSounds.add(entry);voices++;source.start(now);source.stop(now+duration+.01);source.onended=()=>{if(liveSounds.delete(entry))voices--;source.disconnect();if(filter)filter.disconnect();gain.disconnect()}")
insert=h.index('function addActivationFx(')
h=h[:insert]+'''function stopSounds(){for(const e of liveSounds){try{e.source.stop()}catch(error){}e.source.disconnect();e.gain.disconnect()}liveSounds.clear();voices=0}
function preparePop(b){let peak=0;for(let c=0;c<b.numberOfChannels;c++)for(const x of b.getChannelData(c))peak=Math.max(peak,Math.abs(x));let onset=0;for(let i=0;i<b.length;i++){let v=0;for(let c=0;c<b.numberOfChannels;c++)v=Math.max(v,Math.abs(b.getChannelData(c)[i]));if(v>peak*.12){onset=Math.max(0,i-Math.round(b.sampleRate*.001));break}}const length=Math.min(b.length-onset,Math.round(b.sampleRate*.14)),out=audioCtx.createBuffer(b.numberOfChannels,length,b.sampleRate);let energy=0;for(let c=0;c<b.numberOfChannels;c++){const a=b.getChannelData(c),z=out.getChannelData(c);for(let i=0;i<length;i++){z[i]=a[i+onset]*Math.min(1,(length-1-i)/(b.sampleRate*.008));energy+=z[i]*z[i]}}const rms=Math.sqrt(energy/(length*b.numberOfChannels)),gain=Math.min(.65/(peak||1),.008/(rms||1));for(let c=0;c<out.numberOfChannels;c++){const z=out.getChannelData(c);for(let i=0;i<z.length;i++)z[i]*=gain}return out}
function preloadPop(){if(!audioCtx)return Promise.resolve();if(!popReady)popReady=Promise.all(POP_ASSETS.map(async a=>{const data=Uint8Array.from(atob(a.base64),c=>c.charCodeAt(0));popBuffers[a.id]=preparePop(await audioCtx.decodeAudioData(data.buffer))}));return popReady}
function flushImpacts(){const batch=impactBatch;impactBatch=[];if(!batch.length)return;if(audioMode==='synth'){for(const n of batch)sound('hit',n.depth);return}if(!audioCtx||muted||audioCtx.state!=='running'||!popBuffers[audioMode])return;
 // A dedicated four-voice transient pool; optional synthesized sounds never take its slots.
 const active=[...liveSounds].filter(e=>e.kind==='pop');if(active.length>=4){const oldest=active[0];oldest.source.stop();oldest.gain.disconnect();liveSounds.delete(oldest)}
 const t=audioCtx.currentTime,s=audioCtx.createBufferSource(),g=audioCtx.createGain();s.buffer=popBuffers[audioMode];s.playbackRate.value=[1,.99,1.015,.985][popCounter++%4];g.gain.value=Math.min(1.2,1+(batch.length-1)*.04);s.connect(g);g.connect(master);const entry={source:s,gain:g,kind:'pop'};liveSounds.add(entry);s.start(t);s.onended=()=>{liveSounds.delete(entry);s.disconnect();g.disconnect()};popLog.push({time:t,count:batch.length,indices:batch.map(n=>n.index),rate:s.playbackRate.value,attempt:attemptId});
}
''' +h[insert:]
# Collect real activation events; do not precompute a timeline.
h=h.replace("addActivationFx(node);sound('hit',depth);if(mode==='blast')sound('explosion',depth)", "addActivationFx(node);impactBatch.push(node);hitLog.push({index,depth,time:audioCtx?audioCtx.currentTime:0,attempt:attemptId})")
start=h.index('function startAttempt(');end=h.index('\nfunction triggerCell',start)
h=h[:start]+'''async function startAttempt(index){if(running||result||starting||!nodes[index])return;starting=true;const id=attemptId;message.textContent='音频准备中…';try{await ensureAudio();if(audioMode!=='synth')await preloadPop();if(id!==attemptId||document.hidden)return;starting=false;running=true;combo=0;lastSeed=index;sound('charge');activateNode(index,0,true);updateUI()}catch(error){if(id!==attemptId)return;starting=false;message.textContent='音频加载失败，请切换原合成音效';console.error(error)}}
''' +h[end:]
# Keep original simulation traversal, flush runtime batch after a tick.
h=h.replace("sound('fire');if(mode==='blast')sound('explosion')", "sound('fire');impactBatch.push(n);hitLog.push({index:n.index,depth:0,time:audioCtx?audioCtx.currentTime:0,attempt:attemptId})")
h=h.replace('if(!pulses.length)finishRound()}', 'flushImpacts();if(!pulses.length)finishRound()}')
# Replace only Blast node rendering; Classic body retained verbatim.
a=h.index(" if(mode==='blast'&&n.active&&n.fired&&age>200)");b=h.index(' const r=b.nodeR*pop;',a)
h=h[:a]+''' if(mode==='blast'&&n.active&&(!n.seed||n.fired)){ctx.globalAlpha=.25;ctx.strokeStyle='#65736b';ctx.lineWidth=1.2;ctx.beginPath();ctx.arc(0,0,b.nodeR,0,Math.PI*2);ctx.stroke();const d=DIRS[n.dir];ctx.rotate(Math.atan2(d.dy,d.dx));ctx.strokeStyle='#253b32';ctx.lineWidth=2.7;ctx.lineCap='round';ctx.lineJoin='round';ctx.beginPath();ctx.moveTo(-9,0);ctx.lineTo(9,0);ctx.moveTo(3,-6);ctx.lineTo(9,0);ctx.lineTo(3,6);ctx.stroke();ctx.restore();continue}
 let pop=1;if(age<100&&n.seed)pop=1-.15*Math.sin(age/100*Math.PI/2);else if(age<360)pop=1+.22*Math.exp(-age/150)*Math.sin(age/45);
''' +h[b:]
# Blast ring/fragment timing; Classic remains baseline.
h=h.replace('ring.life-=dt/420','ring.life-=dt/(mode===\'blast\'?140:420)').replace('part.life-=dt/380','part.life-=dt/(mode===\'blast\'?140:380)')
h=h.replace("ctx.fillRect(-2,-1,4*part.life,2*part.life)","if(mode==='blast'){ctx.beginPath();ctx.moveTo(-3,-2);ctx.lineTo(4,0);ctx.lineTo(0,3);ctx.fill()}else ctx.fillRect(-2,-1,4*part.life,2*part.life)")
h=h.replace('ensureAudio();sound(\'ui\');resetLevel()', 'ensureAudio();resetLevel()')
h=h.replace("sound('ui');currentLevel=", "lastSeed=null;currentLevel=")
h=h.replace("master.gain.value=muted?0:.65", "master.gain.value=muted?0:volume")
h=h.replace('muted=!muted;try', 'muted=!muted;if(muted)stopSounds();try')
h=h.replace("if(document.hidden)audioCtx.suspend().catch(()=>{})", "if(document.hidden){attemptId++;starting=false;impactBatch=[];stopSounds();audioCtx.suspend().catch(()=>{})}")
h=h.replace('audioState:audioCtx?audioCtx.state:null,mode,theme,voices,','audioMode,lastSeed,starting,hitLog,popLog,popVoices:[...liveSounds].filter(e=>e.kind===\'pop\').length,popDecoded:Object.keys(popBuffers).length,audioState:audioCtx?audioCtx.state:null,mode,theme,voices,')
h=h.replace('setLevel(i){currentLevel=i;resetLevel()}','setLevel(i){currentLevel=i;lastSeed=null;resetLevel()},setAudio(a){audioMode=a;document.getElementById("audioSelect").value=a;resetLevel()},ready:async()=>{await ensureAudio();await preloadPop()}')
h=h.replace('if(debug)window.chainShot={','if(debug)window.chainShot={get audioBuffers(){return popBuffers},')
h=h.replace('resize();applyMode();requestAnimationFrame(frame);', '''const audioSelect=document.getElementById('audioSelect');audioSelect.value=audioMode;audioSelect.addEventListener('change',()=>{audioMode=audioSelect.value;resetLevel();ensureAudio();preloadPop();});
const levelSelect=document.getElementById('levelSelect');LEVELS.forEach((l,i)=>{const o=document.createElement('option');o.value=i;o.textContent=`${i+1} · ${l.name}`;levelSelect.append(o)});levelSelect.addEventListener('change',()=>{currentLevel=Number(levelSelect.value);lastSeed=null;resetLevel()});
document.getElementById('volume').addEventListener('input',ev=>{volume=Number(ev.target.value);if(master)master.gain.value=muted?0:volume});
document.getElementById('replayBtn').addEventListener('click',()=>{if(lastSeed===null)return;const seed=lastSeed;resetLevel();startAttempt(seed)});
resize();applyMode();ensureAudio(false);preloadPop().catch(()=>{message.textContent='Pop加载失败，可使用原合成Hit'});requestAnimationFrame(frame);''')
h=h.replace("audioCtx.suspend().catch(()=>{})};else","audioCtx.suspend().catch(()=>{})}else")
h=h.replace('node.activatedAt=performance.now();activatedCount++','node.activatedAt=performance.now();node.ruptureAt=node.activatedAt;activatedCount++')
h=h.replace('n.fired=true;if(n.seed)','n.fired=true;if(n.seed)n.ruptureAt=performance.now();if(n.seed)')
h=h.replace("if(mode==='blast'&&n.active&&(!n.seed||n.fired)){ctx.globalAlpha", "if(mode==='blast'&&n.active&&(!n.seed||n.fired)){if(now-n.ruptureAt<16){ctx.fillStyle='#ffffff';ctx.beginPath();ctx.arc(0,0,b.nodeR+2,0,Math.PI*2);ctx.fill()}ctx.globalAlpha")
h=h.replace('ensureAudio();preloadPop();','ensureAudio();preloadPop().catch(()=>{message.textContent="Pop unavailable; select synthesized Hit"});')
# UI functions only called after selectors are populated.
(root/'prototype/chain-shot-v0.3.1.html').write_text(h,encoding='utf8')
