import pathlib,json,random,importlib.machinery,re
s=importlib.machinery.SourceFileLoader('solver','tools/chain-shot-solver.py').load_module()
h=pathlib.Path('prototype/chain-shot-v0.2.html').read_text(encoding='utf8')
raw=re.search(r'const LEVELS=(\[.*?\]);',h,re.S)[1];raw=re.sub(r'(solution|nodes|x|y|dir):',r'"\1":',raw);old=json.loads(raw)
shapes=json.loads(pathlib.Path('prototype/chain-shot-v0.2-levels.json').read_text(encoding='utf8'))
levels=[dict(old[0],name='第一推动',intent='观察向左射线穿过节点，再折向上方。'),dict(old[1],name='一线分叉',intent='纵向射线穿过两点，分开触发横向和斜向路径。')]
specs=[('折返',[(1,2),(2,2),(3,2),(4,2),(4,3),(4,4),(2,4),(1,4)],3),('交汇',[(1,1),(3,1),(5,1),(1,3),(3,3),(5,3),(1,5),(3,5),(5,5)],3),('闪电',None,3),('双环',[(1,1),(2,1),(3,1),(3,2),(3,3),(2,3),(1,3),(1,2),(4,3),(5,3),(5,4),(5,5)],5),('爱心',None,7),('房屋',None,4),('回旋',[(1,1),(2,1),(3,1),(4,1),(5,1),(5,2),(5,3),(5,4),(5,5),(4,5),(3,5),(2,5),(1,5),(1,4),(1,3),(1,2)],5),('终章 · 共振',[(1,1),(2,1),(3,1),(4,1),(5,1),(1,3),(2,3),(3,3),(4,3),(5,3),(1,5),(2,5),(3,5),(4,5),(5,5),(2,7),(3,7),(4,7)],6)]
rng=random.Random(303)
for name,points,depth in specs:
 if points is None:l=next(dict(a) for a in shapes if a['name']==name)
 else:
  for attempt in range(300000):
   l=dict(name=name,nodes=[dict(x=x,y=y,dir=rng.choice(list(s.DIRS))) for x,y in points]);r=s.solve(l)
   if r['solutionCount']==1 and r['nearMissCount']>=2 and any(a['reachRatio']==1 and a['cascadeDepth']>=depth and a['branchEvents']>=2 for a in r['seeds']):l['solution']=r['solutionSeeds'][0];break
  else:raise ValueError(name)
 l['intent']={'折返':'追踪两次折向，排除只覆盖局部的起点。','交汇':'区分横纵射线和斜向交汇，观察未连通角点。','闪电':'长斜线与横向分叉，错误起点漏掉上端。','双环':'两个局部回路通过桥接方向接通；从下游启动会漏上游。','爱心':'熟悉轮廓掩盖七代依赖；必须从源头进入，不能只点中心。','房屋':'屋顶与底边的多路交汇，识别向屋顶的回传。','回旋':'沿外环追踪多次转向，同时识别跨环射线。','终章 · 共振':'三条水平层和下端支路共同展开，排除下游近似全清的起点。'}[name]
 levels.append(l)
pathlib.Path('prototype/chain-shot-v0.3-levels.json').write_text(json.dumps(levels,ensure_ascii=False,indent=2),encoding='utf8')
pathlib.Path('tools/chain-shot-v0.3-results.json').write_text(json.dumps([dict(name=l['name'],**s.solve(l)) for l in levels],ensure_ascii=False,indent=2),encoding='utf8')
for l in levels:
 r=s.solve(l);a=r['seeds'][l['solution']];print(l['name'],len(l['nodes']),r['solutionCount'],r['nearMissCount'],a['cascadeDepth'],a['branchEvents'])
