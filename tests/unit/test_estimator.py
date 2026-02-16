import unittest

from backend.src.services.estimator import estimate_payout


class TestEstimator(unittest.TestCase):
    def test_estimate_applies_deductible_and_limit(self):
        res = estimate_payout({'limit':1000}, 1500, deductible=200)
        self.assertEqual(res['estimated_payout'], 1000)


if __name__ == '__main__':
    unittest.main()
