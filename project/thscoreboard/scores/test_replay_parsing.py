from os import path
import unittest

from . import replay_parsing


class Th06ReplayTestCase(unittest.TestCase):

    def ParseTestReplay(self, filename):
        with open(path.join('scores/replays_for_tests', filename), 'rb') as f:
            return replay_parsing.Parse(f.read())
    
    def testHard1cc(self):
        replay_info = self.ParseTestReplay('th6_hard_1cc.rpy')
        self.assertEqual(replay_info.game, 'th06')
        self.assertEqual(replay_info.difficulty, 2)
        self.assertEqual(replay_info.shot, 'ReimuA')
        self.assertEqual(replay_info.score, 92245410)

        # 6 stages (Hard 1cc)
        # Final score is 92245410
        # Final resources are 0 lives, 2 bombs
