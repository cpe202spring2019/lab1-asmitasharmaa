import unittest
from location import *

class TestLab1(unittest.TestCase):
    
    #testing my repr function
    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")
        loc4 = loc1
        self.assertEqual(repr(loc4),"Location('SLO', 35.3, -120.7)")
    
    #testing my eq function
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertFalse(loc1 == loc2)
        loc3 = loc1
        self.assertTrue(loc1 == loc3) 
        loc4 = Location("SLO", 35.30000001, -120.6999999)
        self.assertTrue(loc1 == loc4)
        loc3 = Location("Paris", 48.901, 2.4001)
        self.assertFalse(loc1 == loc3)
        

if __name__ == "__main__":
        unittest.main()
