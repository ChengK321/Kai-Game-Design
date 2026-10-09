"""Endless Peel V0.3 proof-of-mechanics. No external dependencies.

Deterministic per-step spawn tapes create paired comparison across policies.
No model of player skill is claimed: simple heuristics are engineering probes only.
"""
from dataclasses import dataclass
from collections import Counter
from statistics import mean, median
import json, random, argparse

@dataclass(frozen=True)
class Config:
    rows:int=4
    colors:int=4
    initial:int=4
    cap:int=10
    births:int=4
    max_turns:int=150
    spawn_mode:str='random' # random row vs one per row (if births==rows)


def exposed(state):
    return sorted({c for r in state if r for c in (r[0],r[-1])})

def step_peel(state,color):
    out=[]
    total=0
    per_row=[]
    for r in state:
        xs=list(r)
        before=len(xs)
        while xs and xs[0]==color: xs.pop(0)
        while xs and xs[-1]==color: xs.pop()
        # NOTE: both while loops are enough because a remaining color after removing a suffix
        # must already have been at the head before suffix removal, except when empty.
        n=before-len(xs)
        total+=n; per_row.append(n); out.append(tuple(xs))
    return tuple(out),total,per_row

def seeded_state(seed,cfg):
    rng=random.Random(seed ^ 0xA5A52026)
    return tuple(tuple(rng.randrange(cfg.colors) for _ in range(cfg.initial)) for i in range(cfg.rows))

def make_spawn_tape(seed,cfg):
    rng=random.Random(seed+999_993)
    batches=[]
    for _ in range(cfg.max_turns):
        if cfg.spawn_mode=='balanced':
            rr=list(range(cfg.rows));rng.shuffle(rr)
            rix=(rr*(1+cfg.births//cfg.rows))[:cfg.births]
        else:
            rix=[rng.randrange(cfg.rows) for _ in range(cfg.births)]
        batches.append([(row,rng.randrange(2),rng.randrange(cfg.colors)) for row in rix])
    return batches

def born(state,batch,cfg):
    s=[list(r) for r in state]
    for row,side,color in batch:
        if side==0:s[row].insert(0,color)
        else:s[row].append(color)
    return tuple(tuple(r) for r in s)

def pressure(s):
    lengths=[len(r) for r in s]
    return sum(k*k for k in lengths)

def frontier(s):
    return max([step_peel(s,c)[1] for c in exposed(s)] or [0])

def choose(s,policy,cfg,tape,turn,seed):
    opts=exposed(s)
    if not opts:return None
    if policy=='random':
        return random.Random(seed*100_000+turn*431+17).choice(opts)
    val=[]
    for c in opts:
        p,count,_=step_peel(s,c)
        if policy=='greedy': score=float(count)
        elif policy=='pressure': score=count - 0.030*pressure(p)
        elif policy=='lookahead': score=count + 0.80*frontier(p) - 0.018*pressure(p)
        elif policy=='preview':
            sp=born(p,tape[turn],cfg)
            score=count + .80*frontier(sp) - .020*pressure(sp)
        else:raise ValueError(policy)
        val.append((score,count,-int(c),c))
    return max(val)[3]

def play(seed,cfg,policy,trace=False):
    s=seeded_state(seed,cfg)
    tape=make_spawn_tape(seed,cfg)
    removed=0; peak_chain=0; choices=[]; history=[]
    for turn in range(cfg.max_turns):
        opts=exposed(s)
        if not opts: break
        move=choose(s,policy,cfg,tape,turn,seed)
        nxt,n,per=step_peel(s,move)
        peak_chain=max(peak_chain,n)
        removed+=n
        choices.append(len(opts))
        after=born(nxt,tape[turn],cfg)
        if trace and turn<20:
            history.append({'turn':turn+1,'before':[''.join(map(str,r)) for r in s],
                            'opts':opts,'chosen':move,'removed':n,'after':[''.join(map(str,r)) for r in after]})
        s=after
        if max(map(len,s))>cfg.cap:return {'turns':turn+1,'survived':False,'removed':removed,
                   'max_chain':peak_chain,'choice_mean':mean(choices),'trace':history}
    return {'turns':cfg.max_turns,'survived':True,'removed':removed,
            'max_chain':peak_chain,'choice_mean':mean(choices) if choices else 0,'trace':history}

def summarize(values,cfg,policy):
    turns=sorted(x['turns'] for x in values);cnt=len(turns)
    return {'births':cfg.births,'colors':cfg.colors,'cap':cfg.cap,'spawn':cfg.spawn_mode,
            'strategy':policy,'runs':cnt,'mean':round(mean(turns),1), 'median':round(median(turns),1),
            'p10':turns[int(.10*(cnt-1))],'p90':turns[int(.90*(cnt-1))],
            'survive_cap_pct':round(100*sum(x['survived'] for x in values)/cnt,1),
            'mean_removed':round(mean(x['removed'] for x in values),1),
            'mean_options':round(mean(x['choice_mean'] for x in values),2),
            'max_chain_mean':round(mean(x['max_chain'] for x in values),1)}

def run_grid(seeds=300):
    results=[]
    for colors,births,spawn in [(4,3,'random'),(4,4,'random'),(4,5,'random'),
                                 (3,4,'random'),(5,4,'random'),(4,4,'balanced')]:
        cfg=Config(colors=colors,births=births,spawn_mode=spawn)
        for policy in ['random','greedy','pressure','lookahead','preview']:
            values=[play(i,cfg,policy) for i in range(seeds)]
            results.append(summarize(values,cfg,policy))
    return results

def find_non_greedy(cfg, limit=100):
    # Specific replayable counterexamples where lookahead picks something other than immediate best.
    for seed in range(limit):
        s=seeded_state(seed,cfg);tape=make_spawn_tape(seed,cfg)
        for turn in range(min(35,cfg.max_turns)):
            greedy=choose(s,'greedy',cfg,tape,turn,seed)
            future=choose(s,'lookahead',cfg,tape,turn,seed)
            if greedy!=future:
                a=step_peel(s,greedy)[1];b=step_peel(s,future)[1]
                if a>b:
                    return {'seed':seed,'turn':turn+1,'rows':[''.join(map(str,r)) for r in s],
                            'greedy_color':greedy,'greedy_removed':a,
                            'future_color':future,'future_removed':b,
                            'frontiers_after':{str(c):frontier(step_peel(s,c)[0]) for c in exposed(s)}}
            s=born(step_peel(s,future)[0],tape[turn],cfg)
            if max(map(len,s))>cfg.cap:break
    return None

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--seeds',type=int,default=300)
    parser.add_argument('--out',default='')
    a=parser.parse_args()
    cfg=Config()
    res={'method':'v0.3 per-turn paired RNG, visible vs hidden spawn heuristics',
         'seed_count':a.seeds,'table':run_grid(a.seeds),
         'sample_non_greedy':find_non_greedy(cfg),
         'example_trace':play(7,cfg,'lookahead',True)['trace'][:8]}
    if a.out:
        with open(a.out,'w',encoding='utf8') as f:json.dump(res,f,ensure_ascii=False,indent=2)
    for x in res['table']:print(f"{x['colors']}C/{x['births']}B/{x['spawn'][:3]}  {x['strategy']:10} median={x['median']:>5} mean={x['mean']:>6} p10={x['p10']:>3} p90={x['p90']:>3} capped={x['survive_cap_pct']:>5}% opts={x['mean_options']}")
    print('COUNTEREXAMPLE:',res['sample_non_greedy'])
