import pathlib,json
p=pathlib.Path('tools/chain-shot-solver.py');s=p.read_text(encoding='utf-8-sig').replace("levels.json').read_text()","levels.json').read_text(encoding='utf8')");p.write_text(s,encoding='utf8')
import importlib.machinery
solver=importlib.machinery.SourceFileLoader('solver',str(p)).load_module()
levels=json.loads(pathlib.Path('prototype/chain-shot-v0.2-levels.json').read_text(encoding='utf8'))
pathlib.Path('tools/chain-shot-solver-results.json').write_text(json.dumps([dict(name=l['name'],**solver.solve(l)) for l in levels],ensure_ascii=False,indent=2),encoding='utf8')
h=pathlib.Path('prototype/chain-shot-v0.2.html').read_text(encoding='utf8')
expected=[[solver.solve(l)['seeds'][i]['activated'] for i in range(len(l['nodes']))] for l in levels]
test='<script>const expected='+json.dumps(expected)+';</script>'+'''<script>setTimeout(()=>{try{const g=window.chainShot;let checks=0;for(const mode of ['A','B','C']){g.setMode(mode);g.levels.forEach((l,i)=>{for(let seed=0;seed<l.nodes.length;seed++){g.setLevel(i);g.start(seed);g.start((seed+1)%l.nodes.length);let ticks=0;while(g.state.running&&ticks++<200)g.step();if(ticks>=200||JSON.stringify(g.state.active)!==JSON.stringify(g.closure(l,seed)))throw Error(mode+' '+i+' '+seed);if(mode==='C'&&JSON.stringify(g.state.active)!==JSON.stringify(expected[i][seed]))throw Error('offline solver mismatch');checks++}g.setLevel(i);g.start(l.solution);while(g.state.running)g.step();if(g.state.result!=='success')throw Error('demo');g.reset();if(g.state.active.length||g.state.pulses||g.state.result)throw Error('reset')})}g.setMode('C');document.body.dataset.test='PASS '+checks+' seeds';document.body.dataset.overflow=document.documentElement.scrollWidth>innerWidth;document.body.dataset.dpr=devicePixelRatio}catch(e){document.body.dataset.test='FAIL '+e.stack}},100);</script>'''
pathlib.Path('prototype/.v02-browser-test.html').write_text(h.replace('</body>',test+'</body>'),encoding='utf8')
