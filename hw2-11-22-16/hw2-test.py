#######################################
# Caroline Jaffe
# MAS.500, Fall 2016
# hw2-test.py
#	Unit tests for hw2.py
#######################################

import unittest
from hw2 import MediaCloud

class Hw2Test(unittest.TestCase):

    def setUp(self):
        self.mc = MediaCloud()

    def testCreate(self):
        assert self.mc is not None

    def testCount(self):
        self.count = self.mc.getSentenceCount('clinton')
        assert self.count > 0

# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
