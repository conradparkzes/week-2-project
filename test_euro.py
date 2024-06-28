import unittest
from euros import getMatches

class TestEuros(unittest.TestCase):

    def test_getMatches(self):
        test_1 = [{'stage':'groupStage', 'team_a':'germany', 
                        'team_b':'scotland', 'team_a_score':5, 'team_b_score':1,
                        'winning team':'germany', 'expectation':'+2 germany'}]
        self.assertEqual(getMatches(), test_1)

    def test_getMatches2(self):
        test_2 = [{'stage':'groupStage', 'team_a':'netherlands', 'team_b':'austria', 
                        'team_a_score':2, 'team_b_score':3, 'winning team':'austria',
                        'expectation':'+1 netherlands'}]
        self.assertEqual(getMatches(), test_2)

    def test_getMatches3(self):
        test_3 = [{'stage':'groupStage', 'team_a':'france', 'team_b':'poland', 
                        'team_a_score':1, 'team_b_score':1, 'winning team':'draw',
                        'expectation':'+2 france'}]
        self.assertEqual(getMatches(), test_3)

    def test_getMatches4(self):
        test_4 = [{}]
        self.assertEqual(getMatches('groupStage', 'spain', 'georgia'), test_4)

