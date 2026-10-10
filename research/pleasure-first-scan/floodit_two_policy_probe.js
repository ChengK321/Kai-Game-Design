// Flood-It V4.0: research-only greedy vs two-step lookahead, no gameplay UI.
// Usage: node floodit_two_policy_probe.js (Node >= 18)
// Colors assigned by deterministic LCG; all tiles are fully visible.
const N = 7, K = 4, SEEDS = 200;
const rand = seed => { let v = seed + 123456; return () => {
  v = (Math.imul(v,1664525) + 1013904223) >>> 0; return v / 4294967296;
}};
function flood(board,mask,c){
  const out=mask.slice(),queue=[];
  for(let i=0;i<out.length;i++) if(out[i]) queue.push(i);
  for(let j=0;j<queue.length;j++){
    const p=queue[j],x=p%N,y=Math.floor(p/N);
    for(const q of [x>0?p-1:-1,x<N-1?p+1:-1,y>0?p-N:-1,y<N-1?p+N:-1]){
      if(q>=0&&!out[q]&&board[q]===c){out[q]=true;queue.push(q)}
    }
  }
  return out;
}
const count=m=>m.reduce((n,v)=>n+(v?1:0),0);
function play(board,depth){
  let mask=Array(N*N).fill(false);mask[0]=true;mask=flood(board,mask,board[0]);
  let curr=board[0],steps=0;
  while(count(mask)<N*N&&steps<70){
    const options=[];
    for(let c=0;c<K;c++)if(c!==curr){
      const next=flood(board,mask,c),g=count(next);
      let future=g;
      if(depth===2)for(let cc=0;cc<K;cc++)if(cc!==c)
        future=Math.max(future,count(flood(board,next,cc)));
      options.push({c,next,g,future});
    }
    options.sort((a,b)=>b.future-a.future||b.g-a.g||a.c-b.c);
    const best=options[0];mask=best.next;curr=best.c;steps++;
  }
  return steps;
}
const results=[];
for(let seed=0;seed<SEEDS;seed++){
 const r=rand(seed),board=Array.from({length:N*N},()=>Math.floor(r()*K));
 results.push([seed,play(board,1),play(board,2)]);
}
const median=items=>{const x=items.slice().sort((a,b)=>a-b),h=SEEDS/2;return(x[h-1]+x[h])/2};
const sum=items=>items.reduce((a,b)=>a+b,0);
const a=results.map(x=>x[1]),b=results.map(x=>x[2]);
console.log(JSON.stringify({
 boards:SEEDS,grid:`${N}x${N}`,colors:K,
 greedy:{mean:sum(a)/SEEDS,median:median(a)},
 lookahead2:{mean:sum(b)/SEEDS,median:median(b)},
 comparison:{better:results.filter(x=>x[2]<x[1]).length,
 same:results.filter(x=>x[2]===x[1]).length,
 worse:results.filter(x=>x[2]>x[1]).length},
 sourceNotes:"Heuristic baseline only; neither optimal policy nor human playtest."
},null,2));
