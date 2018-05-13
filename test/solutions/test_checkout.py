import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkoutFormat(self):
        self.assertEqual(checkout('A'), -1)
        self.assertEqual(checkout('A3B1'), -1)
        self.assertEqual(checkout('A*3B'), -1)
        self.assertEqual(checkout('A*3'), -1)
        self.assertEqual(checkout('A*1,B*2'), -1)
        self.assertEqual(checkout([''], 0)
        self.assertEqual(checkout(['A'], 50)

if __name__ == '__main__':
    unittest.main()
