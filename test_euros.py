import unittest
from euros import getMatches

class TestEuros(unittest.TestCase):

    def test_getMatches(self):
        test_1 = [{'stage':'groupStage', 'team_a':'germany', 
                      'team_b':'scotland', 'team_a_score':5, 'team_b_score':1,
                      'winning team':'germany', 'expectation':'+2 germany'}]
        self.assertEqual(getMatches('groupStage', 'germany', 'scotland'),test_1)