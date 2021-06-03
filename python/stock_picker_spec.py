# Rewrite this in Unit Test
import unittest
from stock_picker import picker

class StockPickerTestCase(unittest.TestCase):
    """Tests for stock_picker.py"""

    def test_one(self):
        self.assertEqual(picker([17,3,6,9,15,8,6,1,10]), [1,4])
    def test_two(self):
        self.assertEqual(picker([3,17,6,9,18,15,6,1,10]), [0,4])
    def test_three(self):
        self.assertEqual(picker([1,17,6,9,8,15,6,3,19]), [0,8])
    def test_four(self):
        self.assertEqual(picker([19,17,6,9,8,15,6,3,1]), [2,5])
    
if __name__ == '__main__':
    unittest.main()
