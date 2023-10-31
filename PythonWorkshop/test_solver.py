import unittest

from solver import Solver


class MyTestCase(unittest.TestCase):

    def test_negative_discr(self):
        s = Solver()

        self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()

