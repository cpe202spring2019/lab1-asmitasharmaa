import unittest
from lab1 import *

# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    #testing max item
    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        self.assertEqual(max_list_iter([1,2,3]), 3)
        self.assertEqual(max_list_iter([0,9,8]), 9)
        self.assertEqual(max_list_iter([9,0,9,8,7,10]), 10)
        
    def test_max_list2(self):
        # tests for edge cases
        self.assertEqual(max_list_iter([2]),2)
        self.assertEqual(max_list_iter([1,0,1]), 1)
        self.assertEqual(max_list_iter([0,0]), 0)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([-1,-2,-3]),-1)


    #Testing reverse string
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

        #tests for same elements
        self.assertEqual(reverse_rec([0,0,0]),[0,0,0])
        
        #tests for long reverse 
        self.assertEqual(reverse_rec([1,7,3,8,0,2,5,8]),[8,5,2,0,8,3,7,1])
        
        #tests for empty lists
        self.assertEqual(reverse_rec([]), None)
    
    #normal multiple elements list
    def test_bin_search1(self):
        list_val =[0,1,2,3,4,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(9, low, high, list_val), 5)
    
    #normal sorted list
    def test_bin_search2(self):
        list_val =[0,1,2,3,4,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 1)
        self.assertEqual(bin_search(3, low, high, list_val), 3)
    
    #tests for multiple same values
    def test_bin_search3(self):
        list_val =[0,0,1,3,4,5,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 2)
        self.assertEqual(bin_search(0, low, high, list_val), 1)
        self.assertEqual(bin_search(10, low, high, list_val), 6)

    #tests for a very short list
    def test_bin_search4(self):
        list_val =[0,1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 1)
        self.assertEqual(bin_search(0, low, high, list_val), 0)
    
    #a single element list
    def test_bin_search5(self):
        lst = [5]
        self.assertEqual(bin_search(5, 0, len(lst)-1, lst), 0)
        self.assertEqual(bin_search(1, 0, len(lst)-1, lst), None)
        int_val = []
        self.assertEqual(bin_search(1, 0, len(int_val)-1, int_val), None)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)


if __name__ == "__main__":
        unittest.main()

    
