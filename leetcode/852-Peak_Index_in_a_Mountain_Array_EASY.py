# 852-Peak_Index_in_a_Mountain_Array_EASY.py

# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1
# Note:

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.

from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        """Return any indices greater than their neighbors."""

        # Assumptions
        # list fits on single machine or abstracts multi-machine architecture
        # see Note in problem statement

        # Edge cases
        # single mountain

        # Approach
        # Iterate through A starting with second item and going to second-to
        # last item
        # at each iteration check neighbors. If both are smaller than the
        # current item, add the current index to return list

        # Complexity
        # Time O(N) since we iterate through the list once
        # Space O(N) in the worst case if there are many peaks we will have a
        # list close to N/2 (which is still O(N))

        # Potential improvements
        # I can't think of any

        peaks = []

        pointer = 1 # Start at second item
        while pointer < len(A) - 1: # finish at pentultimate item
            if (A[pointer] > A[pointer - 1]) and (A[pointer] > A[pointer + 1]):
                peaks.append(pointer)

            pointer += 1

        return peaks[0]


import unittest

class TestPeakIndexInMountainArray(unittest.TestCase):

    def setUp(self):

        self.solution = Solution()


    # Example 1:

    # Input: [0,1,0]
    # Output: 1
    # Example 2:

    # Input: [0,2,1,0]
    # Output: 1

    def test_example_1(self):
        i = [0,1,0]
        o = 1

        self.assertEqual(self.solution.peakIndexInMountainArray(i), o)

    def test_example_2(self):
        i = [0,2,1,0]
        o = 1

        self.assertEqual(self.solution.peakIndexInMountainArray(i), o)



if __name__ == '__main__':
    unittest.main()









