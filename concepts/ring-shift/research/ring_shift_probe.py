"""Counter-candidate: Ring Shift (移星掠形). Fully synthetic design rule, not original game."""
import random,statistics,collections
N=4
MOVES=[(axis,i,d) for axis in (0,1) for i in range(N) for d in (-1,1)]
def setup(seed):
    rng=random.Random(seed+13579)
    rings=[rng.randrange(4) for _ in range(N*N)]
    cores=[-1]*(N*N)
    for j in rng.sample(range(N*N),8):
        cs=[c for c in range(4) if c!=rings[j]]
        cores[j]=rng.choice(cs)
    randoms=[[rng.random() for k in range(6)] for t in range(100)]
    return rings,cores,randoms

def shift(rings,cores,move):
    axis,i,d=move;old=list(cores)
    idxs=[i*N+j if axis==0 else j*N+i for j in range(N)]
    for j in range(N):
        cores[idxs[(j+d)%N]]=old[idxs[j]]
    num=0
    for j in range(N*N):
        if cores[j]>=0 and cores[j]==rings[j]:cores[j]=-1;num+=1
    return cores,num

def spawn(rings,cores,randoms,births):
    for x in randoms[:births]:
        empty=[i for i,v in enumerate(cores) if v==-1]
        if not empty:return False
        j=empty[int(x*len(empty))]
        # make sure they don't spawn auto-solved
        cores[j]=(rings[j]+1+int(x*3))%4
    return True

def score_move(rings,cores,move):
    x,n=shift(rings,list(cores),move)
    return n,x

def policy(rings,cores,which):
    if which=='random':return None
    outcomes=[]
    for mv in MOVES:
        n,x=score_move(rings,cores,mv)
        if which=='greedy':v=n
        else:
            nextmax=max(score_move(rings,x,m)[0] for m in MOVES)
            v=n+.65*nextmax
        outcomes.append((v,n,mv))
    return max(outcomes)[2]

def play(seed,births=2,which='greedy'):
    rings,cores,tape=setup(seed);r=random.Random(seed*1009+10);zero=0;two=0;cleared=0
    for t in range(100):
        mv=r.choice(MOVES) if which=='random' else policy(rings,cores,which)
        cores,n=shift(rings,cores,mv)
        if n==0:zero+=1
        if n>=2:two+=1
        cleared+=n
        if not spawn(rings,cores,tape[t],births):
            return {'turns':t+1,'cleared':cleared,'zero_ratio':zero/(t+1),'two_ratio':two/(t+1)}
    return {'turns':100,'cleared':cleared,'zero_ratio':zero/100,'two_ratio':two/100}

if __name__=='__main__':
    for births in (1,2,3):
        for policy_name in ('random','greedy','lookahead'):
            data=[play(i,births,policy_name) for i in range(180)]
            turns=[x['turns'] for x in data]
            print(f'births={births} policy={policy_name:10s} median={statistics.median(turns):5.1f} mean={statistics.mean(turns):6.2f} capped={sum(t>=100 for t in turns)/len(turns)*100:4.1f}% zero_clear={statistics.mean(x["zero_ratio"] for x in data)*100:4.1f}% multi_clear={statistics.mean(x["two_ratio"] for x in data)*100:4.1f}%')
