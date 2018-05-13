import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkoutFormat(self):
        self.assertEqual(checkout(''), 0)
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout('a'), 50)
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('BC'), 50)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('D'), 15)
        self.assertEqual(checkout('Axa'), -1)
        self.assertEqual(checkout('-'), -1)
        self.assertEqual(checkout('ABCa'), -1)

if __name__ == '__main__':
    unittest.main()
