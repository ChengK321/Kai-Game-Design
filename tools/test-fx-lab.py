"""Actual Edge/CDP tests. Requires Python websocket-client on the test host only."""
import pathlib,json,subprocess,tempfile,time,urllib.request,base64,importlib.machinery,sys
import websocket
root=pathlib.Path(__file__).resolve().parents[1]
solver=importlib.machinery.SourceFileLoader('solver',str(root/'tools/chain-shot-solver.py')).load_module()
levels=json.loads((root/'prototype/chain-shot-v0.3-levels.json').read_text(encoding='utf8'))
expected=[[s['activated'] for s in solver.solve(l)['seeds']] for l in levels]
edge=pathlib.Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
art=root/'tools/fx-lab-test-artifacts';art.mkdir(exist_ok=True)
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
  url=(root/'prototype/chain-shot-fx-lab.html').as_uri()
  call('Page.navigate',dict(url=url+'?debug=1'))
  for _ in range(50):
   if js('!!window.fxLab'):break
   time.sleep(.1)
  tested=[]
  for sample in ['balloon','balloon2','impact','pluck']:
   for mode in ['classic','blast']:
    for preset in ['single','twelve','medium','dense']:
     js(f"document.getElementById('sample').value='{sample}';document.getElementById('sample').dispatchEvent(new Event('change'));document.getElementById('{mode}').click();fxLab.play('{preset}')")
     stats=js('fxLab.stats');assert stats['hits']=={'single':1,'twelve':12,'medium':12,'dense':18}[preset],stats
     assert stats['audioGroups']>0 and stats['maxPop']<=8 and stats['maxLayers']<=3,stats
     tested.append(dict(sample=sample,mode=mode,preset=preset,hits=stats['hits'],groups=stats['audioGroups'],maxPop=stats['maxPop']))
  js("fxLab.play('twelve')");time.sleep(2)
  sync=js('fxLab.stats.rendered');assert len(sync)==12 and max(e['delayMs'] for e in sync)<75,sync
  decoded=js('fxLab.decoded');assert len(decoded)==4 and all(0<b['duration']<=.141 for b in decoded.values()),decoded
  assert js("fxLab.timeline(BOARDS[0]).events.length") == 12
  assert js("fxLab.timeline(BOARDS[1]).events.length") == 18
  # Match the unchanged game's deterministic waiting/cell-step activation times.
  def activation_times(level):
   ns=level['nodes'];seen={level['solution']};events=[(level['solution'],0)];pulses=[dict(ns[level['solution']],waiting=True)];tick=0
   while pulses:
    tick+=1;moving=pulses;pulses=[]
    for pulse in moving:
     if pulse.pop('waiting',False):pulses.append(pulse);continue
     dx,dy=solver.DIRS[pulse['dir']];pulse['x']+=dx;pulse['y']+=dy
     if not (0<=pulse['x']<7 and 0<=pulse['y']<9):continue
     for i,n in enumerate(ns):
      if i not in seen and n['x']==pulse['x'] and n['y']==pulse['y']:seen.add(i);events.append((i,round(tick*.088,6)));pulses.append(dict(n,waiting=True))
     pulses.append(pulse)
   return events
  for i,j in enumerate([5,9]):
   actual=js(f"fxLab.timeline(BOARDS[{i}]).events.map(e=>[e.index,Number(e.time.toFixed(6))])")
   assert actual==[list(e) for e in activation_times(levels[j])],actual
  layouts=[]
  for width,height,dpr in [(1000,900,1),(390,844,3),(320,568,2)]:
   call('Emulation.setDeviceMetricsOverride',dict(width=width,height=height,deviceScaleFactor=dpr,mobile=width<500));time.sleep(.15)
   assert js('document.documentElement.scrollWidth')<=width,(width,js('({w:innerWidth,scroll:document.documentElement.scrollWidth})'))
   layouts.append([width,height,dpr])
   js("document.getElementById('classic').click();fxLab.stop()")
   (art/f'idle-{width}.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  call('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=2,mobile=True));time.sleep(.15)
  js("document.getElementById('blast').click();fxLab.play('single')")
  time.sleep(.23)
  (art/'blast-impact.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  time.sleep(.45)
  (art/'blast-ghost.png').write_bytes(base64.b64decode(call('Page.captureScreenshot',dict(captureBeyondViewport=True))['data']))
  assert js('fxLab.state.heard > fxLab.state.epoch+.05')
  js("document.getElementById('body').checked=true;document.getElementById('synth').checked=true;fxLab.play('dense')")
  assert js('fxLab.stats.maxLayers')<=3
  js("document.getElementById('mute').checked=true;document.getElementById('mute').dispatchEvent(new Event('change'))")
  assert js('master.gain.value')==0
  js('fxLab.stop()');assert js('fxLab.state.events.length')==0
  # Offline render the prepared sample through the same master/limiter recipe.
  audio=js("""(async()=>{const results=[];for(const [id,b] of Object.entries(buffers)){const c=new OfflineAudioContext(2,44100*3,44100),m=c.createGain(),l=c.createDynamicsCompressor();m.gain.value=.55;l.threshold.value=-12;l.knee.value=3;l.ratio.value=12;l.attack.value=.002;l.release.value=.08;m.connect(l);l.connect(c.destination);for(let i=0;i<12;i++){const s=c.createBufferSource(),g=c.createGain();s.buffer=b;g.gain.value=.89;s.connect(g);g.connect(m);s.start(.1+i*.12)}const out=await c.startRendering();let peak=0;for(let ch=0;ch<2;ch++)for(const v of out.getChannelData(ch)){if(!Number.isFinite(v))throw Error('audio NaN');peak=Math.max(peak,Math.abs(v))}results.push({id,peak})}return results})()""")
  assert all(0<a['peak']<1 for a in audio),audio
  assert not errors,errors
  assert not any(u.startswith(('http:','https:')) for u in events),events
  result=dict(firstFrameDelays=sync,tested=tested,decoded=decoded,offlineAudio=audio,layouts=layouts,consoleErrors=errors,externalRequests=0)
  (art/'results.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(dict(comparisons=len(tested),decoded=decoded,audio=audio,consoleErrors=len(errors))))
 finally:
  proc.terminate();proc.wait(timeout=10)
  try:ws.close()
  except Exception:pass
