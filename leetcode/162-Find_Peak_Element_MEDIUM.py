# 162-Find_Peak_Element_MEDIUM.py

# https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.
# Note:

# Your solution should be in logarithmic complexity.

# Assumptions
# neighbors are distinct, but can be repeated in the array
# nums contains only integers
# nums can contain negative integers or 0
# nums fits in memory on a single machine
# single value should return 0 for the index of the single value
# empty list should return an empty string (from leetcode)
# if no peak, pick second to last element? (from leetcode)

# Approach
# brute force is to look for the first descent. E.g. where nums[i] > nums[i+1]
# this would be O(N) complexity. Since the question wants O(log N) there is
# a better way. Perhaps we can use a binary search method? That is O(log N) bc
# we reduce the search space by 1/2 each iteration. But the array is not
# sorted. If we try to find the max that is O(N) time so no good.
# Say we start in the middle of the array for ex 2:
# mid = 3. then check neighbors. left neighbor is smaller, right neighbor is
# larger. Then check mid of upper half. if right neighbor is smaller then we
# have the answer.

# Complexity
# O(log N) time and O(1) space

# Potential improvements:
# I can't think of any at this time

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if not nums:
            return ''
        if len(nums) == 1:
            return 0

        # Brute force
        # idx = 0
        # while idx < len(nums) - 2:
        #     if nums[idx] > nums[idx + 1]:
        #         return idx

        #     idx += 1

        # return idx

        # Binary search

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1

        return left

# Testcases
# []
# return ''

# [1]
# left = 0; right = 0; mid = 0
# return mid = 0

# [1,2,3,1]
# left = 0; right = 3; mid = 0 + (3 - 0) // 2 = 1
# nums[mid] = 2; nums[mid + 1] = 3
# left = mid = 1; right = 3; mid = 1 + (3 - 1) // 2 = 2
# nums[mid] = 3; nums[mid + 1] = 1
# right = mid = 2; left = 1; mid = 1 + (2 - 1) // 2 = 1


# [1,2,1,3,5,6,4]

# [1,0,-1,0,1]
# left = 0; right = 4; mid = 0 + (4 - 0) // 2 = 2
# nums[mid] = -1 < nums[mid + 1] = 0
# left = mid = 2; right = 4; mid = 2 + (4 - 2) // 2 = 3
# nums[mid] = 0 < nums[mid + 1] = 1

import unittest

class TestFindPeakElement(unittest.TestCase):


    def setUp(self):

        self.solution = Solution()

    def test_example_1(self):
        nums = [1,2,3,1]
        self.assertIn(self.solution.findPeakElement(nums), [2])


    def test_example_2(self):
        nums = [1,2,1,3,5,6,4]
        self.assertIn(self.solution.findPeakElement(nums), [1, 5])


    def test_single(self):
        nums = [1]
        self.assertIn(self.solution.findPeakElement(nums), [0])


    def test_negatives(self):
        nums = [1,0,-1,0,1]
        self.assertIn(self.solution.findPeakElement(nums), [0, 4])


    def test_v(self):
        nums = [3,2,1,2,3]
        self.assertIn(self.solution.findPeakElement(nums), [0, 4])


    def test_a(self):
        nums = [1,2,3,2,1]
        self.assertIn(self.solution.findPeakElement(nums), [2])


    def test_line_ascending(self):
        nums = [-2,-1,0,1,2,3,4,5]
        self.assertIn(self.solution.findPeakElement(nums), [7])


    def test_line_descending(self):
        """Test an array that is descending from the first element."""

        nums = [5,4,3,2,1,0,-1,-2]
        self.assertIn(self.solution.findPeakElement(nums), [0])


if __name__ == '__main__':
    unittest.main()











