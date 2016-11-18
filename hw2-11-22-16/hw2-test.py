#######################################
# Caroline Jaffe
# MAS.500, Fall 2016
# hw2-test.py
#	Unit tests for hw2.py
#######################################

import unittest, datetime, sys
from hw2 import getSentenceCount

class Hw2Test(unittest.TestCase):

    def setUp(self):
        self.results = getSentenceCount('clinton', datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) )

    def testCount(self):
        assert self.results is not None

# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
