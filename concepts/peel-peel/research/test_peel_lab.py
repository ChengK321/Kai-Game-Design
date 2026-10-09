import unittest
from peel_lab import Config,step_peel,born,exposed,play,make_spawn_tape,seeded_state,choose
class PeelRules(unittest.TestCase):
    def test_consecutive_both_sides(self):
        s=(('R','R','B','R'),('B','R','B','R'),('R','R','R'),())
        q,n,per=step_peel(s,'R')
        self.assertEqual(q,(('B',),('B','R','B'),(),()))
        self.assertEqual((n,per),(7,[3,1,3,0]))
    def test_interior_same_color_stays(self):
        q,n,_=step_peel((('B','R','B'),),'R')
        self.assertEqual((q,n),((('B','R','B'),),0))
    def test_only_ends_clickable(self):
        self.assertEqual(exposed((('A','B','C'),('D','A','D'))),['A','C','D'])
    def test_batch_deterministic(self):
        self.assertEqual(make_spawn_tape(17,Config())[:3],make_spawn_tape(17,Config())[:3])
    def test_same_seed_strategy_replay(self):
        self.assertEqual(play(17,Config(),'lookahead'),play(17,Config(),'lookahead'))
    def test_conservation(self):
        s=seeded_state(3,Config());q,n,_=step_peel(s,exposed(s)[0]);n0=sum(map(len,s))
        self.assertEqual(sum(map(len,q))+n,n0)
        self.assertEqual(sum(map(len,born(q,make_spawn_tape(3,Config())[0],Config()))),n0-n+4)
if __name__=='__main__':unittest.main()
