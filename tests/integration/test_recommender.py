import unittest

from backend.src.services.recommender import recommend_claim_type


class Dummy:
    pass


class TestRecommender(unittest.TestCase):
    def test_recommends_burglary_for_theft(self):
        rec = recommend_claim_type('My house was robbed and items stolen', [])
        self.assertIn('Burglary', rec.claim_type)


if __name__ == '__main__':
    unittest.main()
