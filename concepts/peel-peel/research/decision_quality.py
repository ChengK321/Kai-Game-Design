from peel_lab import Config,seeded_state,make_spawn_tape,exposed,choose,step_peel,born
from collections import Counter
from statistics import mean
import json
configs=[Config(colors=4,births=4,cap=8,max_turns=80),
         Config(colors=5,births=4,cap=9,max_turns=80,spawn_mode='balanced')]
all=[]
for cfg in configs:
    count=Counter(); choice_count=Counter(); n_removed=Counter(); first15=[]
    for seed in range(300):
        s=seeded_state(seed,cfg);tape=make_spawn_tape(seed,cfg)
        for t in range(cfg.max_turns):
            opts=exposed(s);choice_count[len(opts)]+=1
            if not opts:break
            greedy=choose(s,'greedy',cfg,tape,t,seed)
            future=choose(s,'lookahead',cfg,tape,t,seed)
            n0=step_peel(s,greedy)[1];n1=step_peel(s,future)[1]
            count['steps']+=1
            if t<15:count['early_steps']+=1
            if greedy!=future:
                count['different_choice']+=1
                if n1<n0:
                    count['short_term_sacrifice']+=1
                    if t<15:count['early_sacrifice']+=1
            n_removed[n1]+=1
            if t<15:first15.append(n1)
            s=born(step_peel(s,future)[0],tape[t],cfg)
            if max(map(len,s))>cfg.cap:break
    result={'setting':cfg.__dict__,'counts':dict(count),
        'sacrifice_of_all_moves_pct':round(count['short_term_sacrifice']/count['steps']*100,1),
        'early_sacrifice_pct':round(count['early_sacrifice']/count['early_steps']*100,1),
        'equal_or_greedy_pct':round((count['steps']-count['short_term_sacrifice'])/count['steps']*100,1),
        'chain_4plus_pct':round(sum(v for n,v in n_removed.items() if n>=4)/count['steps']*100,1),
        'chain_6plus_pct':round(sum(v for n,v in n_removed.items() if n>=6)/count['steps']*100,1),
        'mean_step_clear':round(sum(n*v for n,v in n_removed.items())/count['steps'],2),
        'mean_exposed_colors':round(sum(n*v for n,v in choice_count.items())/count['steps'],2),
        'early_clear_4plus_pct':round(sum(n>=4 for n in first15)/len(first15)*100,1)}
    all.append(result)
    print(result)
with open('decision_quality_300.json','w',encoding='utf8') as f:json.dump(all,f,ensure_ascii=False,indent=2)
