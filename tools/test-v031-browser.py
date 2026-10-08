"""Actual Edge/CDP tests. Requires Python websocket-client on the test host only."""
import pathlib,json,subprocess,tempfile,time,urllib.request,base64,importlib.machinery,sys
import websocket
root=pathlib.Path(__file__).resolve().parents[1]
solver=importlib.machinery.SourceFileLoader('solver',str(root/'tools/chain-shot-solver.py')).load_module()
levels=json.loads((root/'prototype/chain-shot-v0.3-levels.json').read_text(encoding='utf8'))
expected=[[s['activated'] for s in solver.solve(l)['seeds']] for l in levels]
edge=pathlib.Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
art=root/'tools/v031-test-artifacts';art.mkdir(exist_ok=True)
errors=[];events=[];counter=0
with tempfile.TemporaryDirectory(prefix='chain-shot-edge-') as profile:
 proc=subprocess.Popen([str(edge),'--headless','--disable-gpu','--no-sandbox','--remote-debugging-port=9333','--remote-allow-origins=*','--user-data-dir='+profile,'about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 try:
  for _ in range(50):
   try:tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9333/json'));break
   except Exception:time.sleep(.1)
  ws=websocket.create_connection(next(t['webSocketDebuggerUrl'] for t in tabs if t['type']=='page'),timeout=20)
  def call(method,params=None):
   global counter
   counter+=1;ws.send(json.dumps(dict(id=counter,method=method,params=params or {})))
   while True:
    r=json.loads(ws.recv())
    if r.get('method')=='Runtime.exceptionThrown':errors.append(r)
    if r.get('method')=='Runtime.consoleAPICalled' and r['params']['type']=='error':errors.append(r)
    if r.get('method')=='Network.requestWillBeSent':events.append(r['params']['request']['url'])
    if r.get('id')==counter:
     if 'error' in r:raise RuntimeError(r)
     return r.get('result',{})
  def js(expr):
   r=call('Runtime.evaluate',dict(expression=expr,returnByValue=True,awaitPromise=True,userGesture=True))
   if 'exceptionDetails' in r:raise RuntimeError(r)
   return r['result'].get('value')
  call('Runtime.enable');call('Page.enable');call('Network.enable')
  url=(root/'prototype/chain-shot-v0.3.1.html').as_uri()
  call('Page.navigate',dict(url=url+'?debug=1'))
  for _ in range(50):
   if js('!!window.chainShot'):break
   time.sleep(.1)
  if not js('!!window.chainShot'):raise RuntimeError(errors)
  js('chainShot.ready()')
  matrix="""(async()=>{const g=chainShot,expected=EXPECTED;let count=0;for(const visual of ['classic','blast'])for(const audio of ['synth','balloon','balloon2','impact','pluck']){g.setMode(visual);g.setAudio(audio);for(let i=0;i<g.levels.length;i++){const l=g.levels[i];for(let seed=0;seed<l.nodes.length;seed++){g.setLevel(i);await g.start(seed);g.start((seed+1)%l.nodes.length);if(g.state.activatedCount!==1)throw Error('second seed');let t=0;while(g.state.running&&t++<200){if(g.state.result)throw Error('early result');g.step()}if(t>=200||g.state.pulses||JSON.stringify(g.state.active)!==JSON.stringify(expected[i][seed]))throw Error('closure '+i+' '+seed);count++;g.reset();if(g.state.activatedCount||g.state.pulses||g.state.popVoices||g.state.voices||g.state.hitLog.length||g.state.popLog.length)throw Error('reset') }}}return count})()""".replace('EXPECTED',json.dumps(expected))
  count=js(matrix);assert count==1100,count
  # Four candidate assets must decode, and replay/reset must cancel asynchronous start.
  assert js('chainShot.state.popDecoded')==4
  js("chainShot.setLevel(5);chainShot.start(6);chainShot.reset()")
  time.sleep(.1);assert not js('chainShot.state.running or chainShot.state.starting'.replace(' or ',' || '))
  js("chainShot.setLevel(5);chainShot.setAudio('balloon');chainShot.setMode('blast')")
  layouts=[]
  for width,height,dpr in [(1000,900,1),(390,844,3),(320,568,2)]:
   call('Emulation.setDeviceMetricsOverride',dict(width=width,height=height,deviceScaleFactor=dpr,mobile=width<500));time.sleep(.15)
   assert js('document.documentElement.scrollWidth')<=width
   (art/f'idle-{width}.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
   layouts.append([width,height,dpr])
  call('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=2,mobile=True));time.sleep(.15)
  # Real touch with a player's chosen correct Seed on L6.
  def touch_seed(seed):
   p=js(f'chainShot.point({seed})');o=js("(()=>{let r=document.querySelector('canvas').getBoundingClientRect();return {x:r.left,y:r.top}})()")
   call('Emulation.setTouchEmulationEnabled',dict(enabled=True,maxTouchPoints=1))
   call('Input.dispatchTouchEvent',dict(type='touchStart',touchPoints=[dict(x=p['x']+o['x'],y=p['y']+o['y'])]));call('Input.dispatchTouchEvent',dict(type='touchEnd',touchPoints=[]))
  touch_seed(levels[5]['solution']);time.sleep(.6)
  assert js('chainShot.state.running')
  (art/'l6-cascade.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  time.sleep(4);assert js('chainShot.state.result')=='success'
  l6log=js('chainShot.state.popLog');assert sum(e['count'] for e in l6log)==12
  (art/'l6-ghost-success.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  # Same Seed survives mode/audio switches and can be replayed without exposing answer.
  js("document.querySelector('[data-mode=classic]').click();document.getElementById('audioSelect').value='synth';document.getElementById('audioSelect').dispatchEvent(new Event('change'));document.getElementById('replayBtn').click()")
  time.sleep(.2);assert js('chainShot.state.running && chainShot.state.lastSeed===6')
  js('chainShot.reset()');assert js('chainShot.state.voices===0 && chainShot.state.popVoices===0')
  near=next(r['seed'] for r in solver.solve(levels[5])['seeds'] if .6<=r['reachRatio']<=.9)
  js(f"chainShot.setLevel(5);chainShot.setAudio('balloon');chainShot.setMode('blast');chainShot.start({near})")
  time.sleep(4);assert js('chainShot.state.result')=='fail'
  (art/'l6-near-miss.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  js("chainShot.setLevel(9);chainShot.setAudio('balloon');chainShot.setMode('blast')")
  touch_seed(levels[9]['solution']);time.sleep(.4)
  js("document.getElementById('muteBtn').click()")
  assert js('chainShot.state.muted && chainShot.state.voices===0 && chainShot.state.popVoices===0')
  js("document.getElementById('muteBtn').click()")
  time.sleep(4);assert js('chainShot.state.result')=='success'
  # Full, unmuted dense run, recorded actual audio events for offline mix verification.
  js("document.getElementById('replayBtn').click()");time.sleep(4)
  assert js('chainShot.state.result')=='success'
  dense=js('chainShot.state.popLog');assert sum(e['count'] for e in dense)==18,dense
  (art/'l10-ghost-success.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  hits=js('chainShot.state.hitLog');assert len({e['index'] for e in hits})==18
  assert all(abs(h['time']-p['time'])<.02 for p in dense for h in hits if h['index'] in p['indices'])
  # Render the recorded live L10 events through current Pop/master/limiter recipe.
  audio=js("""(async()=>{const out=[];for(const [id,b] of Object.entries(chainShot.audioBuffers)){const c=new OfflineAudioContext(2,44100*5,44100),m=c.createGain(),l=c.createDynamicsCompressor();m.gain.value=.65;l.threshold.value=-18;l.knee.value=12;l.ratio.value=4;m.connect(l);l.connect(c.destination);for(const e of chainShot.state.popLog){const s=c.createBufferSource(),g=c.createGain();s.buffer=b;s.playbackRate.value=e.rate;g.gain.value=Math.min(1.2,1+(e.count-1)*.04);s.connect(g);g.connect(m);s.start(.1+e.time-chainShot.state.popLog[0].time)}const data=await c.startRendering();let peak=0;for(let ch=0;ch<2;ch++)for(const v of data.getChannelData(ch)){if(!Number.isFinite(v))throw Error('nonfinite');peak=Math.max(peak,Math.abs(v))}out.push({id,peak})}return out})()""")
  assert all(0<a['peak']<1 for a in audio),audio
  assert not errors,errors
  assert not any(u.startswith(('http:','https:')) for u in events),events
  result=dict(seedComparisons=count,layouts=layouts,l6Pop=l6log,l6NearSeed=near,l10Pop=dense,l10Hits=hits,offlineAudio=audio,consoleErrors=errors,externalRequests=0)
  (art/'results.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(dict(seedComparisons=count,nearSeed=near,denseHits=len(hits),audio=audio,errors=len(errors))))
 finally:
  proc.terminate();proc.wait(timeout=10)
  try:ws.close()
  except Exception:pass
