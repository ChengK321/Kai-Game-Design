"""Actual Edge/CDP tests. Requires Python websocket-client on the test host only."""
import pathlib,json,subprocess,tempfile,time,urllib.request,base64,importlib.machinery,sys
import websocket
root=pathlib.Path(__file__).resolve().parents[1]
solver=importlib.machinery.SourceFileLoader('solver',str(root/'tools/chain-shot-solver.py')).load_module()
levels=json.loads((root/'prototype/chain-shot-v0.3-levels.json').read_text(encoding='utf8'))
expected=[[s['activated'] for s in solver.solve(l)['seeds']] for l in levels]
edge=pathlib.Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
art=root/'tools/v03-test-artifacts';art.mkdir(exist_ok=True)
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
   r=call('Runtime.evaluate',dict(expression=expr,returnByValue=True,awaitPromise=True))
   if 'exceptionDetails' in r:raise RuntimeError(r)
   return r['result'].get('value')
  call('Runtime.enable');call('Page.enable');call('Network.enable')
  url=(root/'prototype/chain-shot-v0.3.html').as_uri()
  call('Page.navigate',dict(url=url+'?debug=1'))
  for _ in range(50):
   if js('!!window.chainShot'):break
   time.sleep(.1)
  test="""(()=>{const g=chainShot,expected=EXPECTED;let count=0;for(const mode of ['classic','blast'])for(const theme of ['minimal','direction','palette']){g.setMode(mode);g.setTheme(theme);g.levels.forEach((l,i)=>{for(let seed=0;seed<l.nodes.length;seed++){g.setLevel(i);g.start(seed);g.start((seed+1)%l.nodes.length);if(g.state.activatedCount!==1)throw Error('second Seed');let t=0;while(g.state.running&&t++<200){if(g.state.result)throw Error('early result');g.step();if(g.state.activatedCount>l.nodes.length)throw Error('duplicate')}if(t>=200||g.state.pulses||JSON.stringify(g.state.active)!==JSON.stringify(expected[i][seed]))throw Error('closure '+i+' '+seed);const end=JSON.stringify(g.state.active);g.step();if(end!==JSON.stringify(g.state.active))throw Error('repeat');count++;g.reset();if(g.state.pulses||g.state.rings||g.state.particles||g.state.result||g.state.activatedCount)throw Error('reset') }g.setLevel(i);g.start(l.solution);while(g.state.running)g.step();if(g.state.result!=='success')throw Error('Demo');document.getElementById('nextBtn').click();if(g.state.result||g.state.activatedCount)throw Error('next')})}g.setLevel(9);g.start(g.levels[9].solution);g.setMode('classic');if(g.state.running||g.state.activatedCount)throw Error('mode switch');return count})()""".replace('EXPECTED',json.dumps(expected))
  count=js(test);assert count==sum(len(l["nodes"]) for l in levels)*6,count
  # Genuine device metrics avoids Edge's minimum native window width.
  layouts=[]
  for width,height,dpr in [(1000,900,1),(390,844,3),(320,568,2),(768,1024,2)]:
   call('Emulation.setDeviceMetricsOverride',dict(width=width,height=height,deviceScaleFactor=dpr,mobile=width<500))
   js("chainShot.setLevel(9);chainShot.setMode('classic');chainShot.setTheme('direction')")
   time.sleep(.15)
   layout=js("""(()=>{const a=document.getElementById('app').getBoundingClientRect(),g=chainShot,c=document.querySelector('.controls').getBoundingClientRect();return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,appHeight:a.height,points:g.levels[9].nodes.map((_,i)=>g.point(i)),controlsTop:c.top-a.top,canvasWidth:document.querySelector('canvas').width}})()""")
   assert layout['scrollWidth']==width,layout
   points=layout['points'];assert min(((a['x']-b['x'])**2+(a['y']-b['y'])**2)**.5 for i,a in enumerate(points) for b in points[i+1:])>=44-1e-6,layout
   assert all(190<p['y']<layout['controlsTop']-44 and 22<p['x']<min(width,520)-22 for p in layout['points']),layout
   layouts.append(dict(width=width,height=height,dpr=dpr,**{k:v for k,v in layout.items() if k not in ('points','width')}))
   if width in (1000,390):
    shot=call('Page.captureScreenshot',dict(format='png',captureBeyondViewport=True));(art/f'idle-{width}.png').write_bytes(base64.b64decode(shot['data']))
  call('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=2,mobile=True))
  time.sleep(.2)
  js("chainShot.setLevel(0);chainShot.setMode('blast');chainShot.setTheme('minimal')")
  for i in range(10):
   js(f"chainShot.setLevel({i});chainShot.setMode('classic');chainShot.setTheme('palette')")
   time.sleep(.06)
   (art/f'level-{i+1:02}.png').write_bytes(base64.b64decode(call('Page.captureScreenshot')['data']))
  js("chainShot.setLevel(0);chainShot.setMode('blast');chainShot.setTheme('minimal')")
  point=js('chainShot.point(chainShot.levels[0].solution)');offset=js("(()=>{let r=document.querySelector('canvas').getBoundingClientRect();return {x:r.left,y:r.top}})()")
  x=point['x']+offset['x'];y=point['y']+offset['y']
  call('Emulation.setTouchEmulationEnabled',dict(enabled=True,maxTouchPoints=1))
  call('Input.dispatchTouchEvent',dict(type='touchStart',touchPoints=[dict(x=x,y=y)]));call('Input.dispatchTouchEvent',dict(type='touchEnd',touchPoints=[]))
  time.sleep(.2);assert js('chainShot.state.running')
  (art/'blast-cascade.png').write_bytes(base64.b64decode(call('Page.captureScreenshot')['data']))
  time.sleep(3);assert js('chainShot.state.result')=='success'
  (art/'blast-success.png').write_bytes(base64.b64decode(call('Page.captureScreenshot')['data']))
  js("document.getElementById('muteBtn').click()");time.sleep(.05);assert js('chainShot.state.muted && chainShot.state.masterGain===0')
  js("document.getElementById('muteBtn').click()");time.sleep(.05);assert js('!chainShot.state.muted && chainShot.state.masterGain>0')
  call('Page.navigate',dict(url=url+'?mode=blast&theme=palette'));time.sleep(.3)
  assert js("!window.chainShot && document.getElementById('demoBtn').hidden && document.getElementById('debugInfo').hidden")
  assert not errors,errors
  assert not any(u.startswith(('http:','https:')) for u in events),events
  html=(root/'prototype/chain-shot-v0.3.html').read_text(encoding='utf8')
  sound_source=html[html.index('function sound('):html.index('function addActivationFx(')].replace("||audioCtx.state!=='running'",'') # Offline context schedules before rendering, unlike the live context.
  audio_test="""(async()=>{const audioCtx=new OfflineAudioContext(1,44100,44100),master=audioCtx.createGain(),compressor=audioCtx.createDynamicsCompressor();let voices=0,muted=false;master.gain.value=.65;compressor.threshold.value=-18;compressor.knee.value=12;compressor.ratio.value=4;master.connect(compressor);compressor.connect(audioCtx.destination);const noise=audioCtx.createBuffer(1,6615,44100);let r=303;for(let i=0;i<6615;i++){r=(r*1664525+1013904223)>>>0;noise.getChannelData(0)[i]=r/4294967296*2-1} SOUND_SOURCE for(let i=0;i<30;i++){sound('hit',i);sound('explosion',i);sound('branch',i)}const maxVoices=voices;const b=await audioCtx.startRendering();let peak=0;for(const x of b.getChannelData(0)){if(!Number.isFinite(x))throw Error('nonfinite audio');peak=Math.max(peak,Math.abs(x))}return {peak,maxVoices}})()""".replace('SOUND_SOURCE',sound_source)
  audio=js(audio_test);assert 0<audio['peak']<.95 and audio['maxVoices']<=12,audio
  result=dict(audioStress=audio,seedComparisons=count,layouts=layouts,touchDemo='PASS',mute='PASS',consoleErrors=errors,externalRequests=0)
  (art/'results.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
 finally:
  proc.terminate();proc.wait(timeout=10)
  try:ws.close()
  except Exception:pass
