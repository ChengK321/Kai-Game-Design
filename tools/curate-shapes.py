import sys,json,random,pathlib
sys.path.insert(0,'tools')
from importlib.machinery import SourceFileLoader
s=SourceFileLoader('solver','tools/chain-shot-solver.py').load_module()
shapes=[('爱心',[(1,2),(2,1),(3,2),(4,1),(5,2),(5,3),(4,4),(3,5),(2,4),(1,3),(3,3)]),('房屋',[(3,1),(2,2),(1,3),(5,3),(4,2),(1,4),(1,5),(2,5),(3,5),(4,5),(5,5),(5,4),(3,3)]),('闪电',[(4,1),(3,2),(2,3),(1,4),(2,4),(3,4),(4,4),(5,4),(4,5),(3,6),(2,7)])]
rng=random.Random(321);levels=[]
for name,points in shapes:
 for attempt in range(200000):
  l=dict(name=name,nodes=[dict(x=x,y=y,dir=rng.choice(list(s.DIRS))) for x,y in points]);r=s.solve(l)
  if r['solutionCount'] in (1,2) and r['nearMissCount']>=2 and any(a['reachRatio']==1 and a['branchEvents']>=1 and a['cascadeDepth']>=3 for a in r['seeds']):
   l['solution']=r['solutionSeeds'][0];levels.append(l);print(name,attempt,r['solutionCount'],r['nearMissCount']);break
 else:raise Exception(name)
pathlib.Path('prototype/chain-shot-v0.2-levels.json').write_text(json.dumps(levels,ensure_ascii=False,indent=2),encoding='utf8')
