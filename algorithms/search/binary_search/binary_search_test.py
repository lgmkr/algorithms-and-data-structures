from binary_search import *
import unittest

class TestBinarySearch(unittest.TestCase):

    def testIsNeedleInArray(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)


    def testIsNeedleNotInArray(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 5), None)

    @unittest.skip(binary_search_leftmost.__doc__)
    def testLeftMostNeedleInArray(self):
        self.assertEqual(binary_search_leftmost([1, 2, 3, 3, 3, 4], 3), 2)

    @unittest.skip(binary_search_leftmost.__doc__)
    def testLeftMostNeedleNotInArray(self):
        self.assertEqual(binary_search_leftmost([1, 2, 3, 3, 3, 4], 5), None)

    @unittest.skip(binary_search_rightmost.__doc__)
    def testRightMostNeedleInArray(self):
        self.assertEqual(binary_search_rightmost([1, 2, 3, 3, 3, 4], 3), 4)

    def testBSRightMostNeedleInArray(self):
        self.assertEqual(bs_rightmost([1, 2, 3, 3, 3, 4], 3), 5)

if __name__ == '__main__':
    unittest.main()
