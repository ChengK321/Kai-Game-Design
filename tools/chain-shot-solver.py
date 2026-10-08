import json,re,random,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
DIRS={'U':(0,-1),'D':(0,1),'L':(-1,0),'R':(1,0),'UL':(-1,-1),'UR':(1,-1),'DL':(-1,1),'DR':(1,1)}
def graph(level):
 ns=level['nodes']; out=[]
 for a in ns:
  dx,dy=DIRS[a['dir']]; hits=[]
  for j,b in enumerate(ns):
   x,y=b['x']-a['x'],b['y']-a['y']
   t=x/dx if dx else y/dy
   if t>0 and x==dx*t and y==dy*t:hits.append((t,j))
  out.append([j for _,j in sorted(hits)])
 return out
def solve(level):
 g=graph(level); results=[]
 for seed in range(len(g)):
  seen={seed}; queue=[seed]; generations={seed:0}; branches=0
  for a in queue:
   new=[b for b in g[a] if b not in seen]
   branches+=len(new)>=2
   for b in new:seen.add(b);queue.append(b);generations[b]=generations[a]+1
  results.append(dict(seed=seed,reachableCount=len(seen),reachRatio=len(seen)/len(g),cascadeDepth=max(generations.values()),branchEvents=branches,generations=generations,activated=sorted(seen)))
 solutions=[r['seed'] for r in results if r['reachRatio']==1]
 return dict(solutionCount=len(solutions),solutionSeeds=solutions,nearMissCount=sum(.6<=r['reachRatio']<=.9 for r in results),seeds=results)
if __name__=='__main__':
 import sys
 levels=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf8')) if len(sys.argv)>1 else json.loads((root/'prototype/chain-shot-v0.2-levels.json').read_text(encoding='utf8'))
 if isinstance(levels,dict):levels=[levels]
 print(json.dumps([dict(name=l.get('name','level'),**solve(l)) for l in levels],ensure_ascii=False,indent=2))
