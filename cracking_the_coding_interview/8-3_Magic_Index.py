# 8-3_Magic_Index.py

# See notebook for discussion

from typing import List

def find_magic_index(A:List) -> int:
    """Find i such that A[i] = i in sorted distinct array of ints or -1."""

    left = 0
    right = len(A) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            right = mid - 1
        elif A[mid] < mid:
            left = mid + 1

    return -1



import unittest

class TestFindMagicIndex(unittest.TestCase):

    def test_example_1(self):

        A = [-1,0,1,2,4,6,7,8,9,10]
        self.assertEqual(4, find_magic_index(A))

    def test_example_2(self):

        A = [-1,0,1,2,3,6,7,8,9,10]
        self.assertEqual(-1, find_magic_index(A))


    def test_edge_cases(self):

        A = [0]
        self.assertEqual(0, find_magic_index(A))

        A = []
        self.assertEqual(-1, find_magic_index(A))





if __name__ == '__main__':
    unittest.main()