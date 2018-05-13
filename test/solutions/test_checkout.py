import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkoutType(self):
        self.assertEqual(checkout(1), -1)

    def test_checkoutFormat(self):
        self.assertEqual(checkout('A*1,B*2'), [['A', 1], ['B', 2]])

if __name__ == '__main__':
    unittest.main()
