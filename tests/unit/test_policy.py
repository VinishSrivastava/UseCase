import unittest

from backend.src.models.policy import Policy


class TestPolicyModel(unittest.TestCase):
    def test_find_clauses(self):
        p = Policy(policy_id='p1', owner_id='u1', text='x', parsed_clauses=[{'id':'c0','text':'Water damage is excluded.'},{'id':'c1','text':'Theft is covered.'}])
        res = p.find_clauses('water')
        self.assertEqual(len(res), 1)


if __name__ == '__main__':
    unittest.main()
