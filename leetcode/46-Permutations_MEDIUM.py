# 46-Permutations_MEDIUM.py

# https://leetcode.com/problems/permutations/

# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

from typing import List

class Solution:

    def __init__(self):
        self.answer = []

    def permute(self, nums: List[int]) -> List[List[int]]:

    # Assumptions
    # integers are distinct
    # data fits on a single machine
    # recursion depth is not exceeded

    # Approach, Complexity, Tradeoffs, Potential Improvements
    # 1. Recursive backtracking approach
    # E.g. we take the first item and recursively call permute on the
    # rest of the list. When we reach the end of the list we add that
    # candidate to our return output.
    # Time complexity is O(N!) but I don't think we can do better since we
    # want ALL the permutations
    # Space complexity is O(N!) since we want all the permutations.
    # 2. implemented recursive, call for each item if that item isn't already
    # in the subset
    # O(N!) time
    # I'm not sure how much time existence check for whether the item is
    # already in the subset adds. It's O(N) but it happens for each item
    # in each subset
    # so maybe overall we are O(N * N!) time and space
    # I'm not sure how to do this better though


    # Edge Cases
    # very large N
    # []
    # single element

        def helper(nums: List, subset: List, i: int) -> None:
            if i == len(nums):
                self.answer.append(subset.copy())

            else:
                for num in nums:
                    if num not in subset:
                        subset[i] = num
                        helper(nums, subset, i + 1)
                        subset[i] = None


        subset = [None] * len(nums)

        helper(nums, subset, 0)

        return self.answer


import unittest

class TestPermute(unittest.TestCase):

    def setUp(self):

        self.solution = Solution()


    def test_example_1(self):

        i = [1,2,3]
        o = [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]


        self.assertEqual(
            sorted(self.solution.permute(i)),
            sorted(o)
        )

    def test_smaller_example(self):

        i = [1,2]
        o = [
          [1,2],
          [2,1]
        ]
        self.assertEqual(
            sorted(self.solution.permute(i)),
            sorted(o)
        )

    def test_single_element(self):

        i = [1]
        o = [
          [1]
        ]
        self.assertEqual(
            sorted(self.solution.permute(i)),
            sorted(o)
        )

    def test_empty_set(self):

        i = []
        o = [
          []
        ]
        self.assertEqual(
            sorted(self.solution.permute(i)),
            sorted(o)
        )


if __name__ == '__main__':
    unittest.main()







