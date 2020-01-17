# 704-Binary_Search_EASY.py

# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Note:

# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].

# Assumptions
# See Notes

# Approach
# Iterative. Check whether target is greater or less than middle value. If
# less then check lower half and discard upper. Repeat until we find the value

# Time and space complexity
# O(log N) since we discard half of N each iteration.

# Potential improvements
# None that I can think of

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        mid = ((right - left) // 2) + left

        while True:


            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1

            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid

            if left >= right:
                break

        return -1


import unittest

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):

        nums = [-1,0,3,5,9,12]
        target = 9
        output = 4

        self.assertEqual(self.solution.search(nums, target), output)

    def test_example_2(self):

        nums = [-1,0,3,5,9,12]
        target = 2
        output = -1

        self.assertEqual(self.solution.search(nums, target), output)

    def test_single_digit_exists(self):

        nums = [1]
        target = 1
        output = 0

        self.assertEqual(self.solution.search(nums, target), output)

    def test_single_digit_not_exists(self):
        nums = [1]
        target = 2
        output = -1

        self.assertEqual(self.solution.search(nums, target), output)


    def test_leetcode_testcase(self):
        nums = [2,5]
        target = 5
        output = 1

        self.assertEqual(self.solution.search(nums, target), output)


if __name__ == '__main__':
    unittest.main()












