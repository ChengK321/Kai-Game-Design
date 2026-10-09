from peel_lab import *
import json
cases=[]
for cap in (8,9,10,12):
 for colors in (4,5):
  for spawn in ('random','balanced'):
   cfg=Config(colors=colors,births=4,spawn_mode=spawn,cap=cap,max_turns=120)
   cases.append(cfg)
for colors in (4,5):
 for cap in (8,9,10):
  cfg=Config(colors=colors,births=3,spawn_mode='random',cap=cap,max_turns=120)
  cases.append(cfg)
all=[]
for cfg in cases:
 val={p:[play(i,cfg,p) for i in range(180)] for p in ('random','greedy','lookahead','preview')}
 items={p:summarize(val[p],cfg,p) for p in val}
 pair=sum(val['lookahead'][i]['turns']>val['greedy'][i]['turns'] for i in range(180))/180
 both=sum(val['lookahead'][i]['turns']==val['greedy'][i]['turns'] for i in range(180))/180
 all.append({'cfg':cfg.__dict__,'by_policy':items,'lookahead_better_pct':round(pair*100,1),'tie_pct':round(both*100,1)})
 print(f"cap={cfg.cap:2} C={cfg.colors} birth={cfg.births} {cfg.spawn_mode:8}  med: " + ' '.join(f'{k[:3]}={items[k]["median"]:>5}' for k in val) + f' better%={pair*100:4.1f}',flush=True)
with open('sensitivity_180.json','w',encoding='utf8') as f:json.dump(all,f,ensure_ascii=False,indent=2)
