import unittest
from lab1 import *

# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([0,0,0]),[0,0,0])
        self.assertEqual(reverse_rec([1,7,3,8,0,2,5,8]),[8,5,2,0,8,3,7,1])
        self.assertEqual(reverse_rec([]), None)

    def test_bin_search1(self):
        list_val =[0,1,2,3,4,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(9, low, high, list_val), 5)

    def test_bin_search2(self):
        list_val =[0,1,2,3,4,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 1)
        self.assertEqual(bin_search(3, low, high, list_val), 3)
    
    def test_bin_search3(self):
        list_val =[0,0,1,3,4,5,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 2)
        self.assertEqual(bin_search(0, low, high, list_val), 1)
        self.assertEqual(bin_search(10, low, high, list_val), 6)

    def test_bin_search4(self):
        list_val =[0,1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 1)
        self.assertEqual(bin_search(0, low, high, list_val), 0)


if __name__ == "__main__":
        unittest.main()

    
