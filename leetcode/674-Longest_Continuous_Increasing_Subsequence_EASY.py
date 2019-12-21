# 674-Longest_Continuous_Increasing_Subsequence_EASY.py


# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # Approach, Time & Space Complexity & Possible Improvements:
        # Approach:
        # loop through each digit with a curr_length and max_length
        # if the next digit is not larger (equal or smaller) than the current
        # then set curr_length equal to the max_length if it is larger
        # then reset the curr_length
        # Time Complexity:
        # O(N) because we go through each item, and perform O(1) operations
        # Space Complexity:
        # O(1) in extra space since we are storing a few integer counters
        # Possible improvements:
        # Stop if there are less items left than the max_length found
        # Since there aren't enough items to beat that max_length we can stop

        if not nums:
            return 0
        if len(nums) < 2:
            return 1

        curr_length = 0
        max_length = 0

        # loop through nums, stopping before last digit
        for idx, num in enumerate(nums[:-1]):

            curr_length += 1

            # if the next digit is equal or smaller update max length
            if nums[idx + 1] <= num:
                # only update max length if curr_length is bigger
                if curr_length > max_length:
                    max_length = curr_length

                # Reset curr_length
                curr_length = 0

        # if the whole list is increasing, then set max_length = curr_length
        # plus the end item which we haven't yet counted
        curr_length += 1
        if curr_length > max_length:
            max_length = curr_length

        return max_length

import unittest

class TestFindLengthOfLCIS(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1,3,5,4,7]
        output = 3
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

    def test_example_2(self):
        nums = [2,2,2,2,2]
        output = 1
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

    def test_small_array_1(self):
        nums = [2]
        output = 1
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

    def test_small_array_2(self):
        nums = []
        output = 0
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

    def test_whole_list_increasing(self):
        nums = [1,3,5,7]
        output = 4
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

    def test_second_part_increasing(self):
        nums = [1,3,2,7,8,9,10,11,12,13]
        output = 8
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

    def test_leetcode_example_1(self):
        nums = [1,3,5,4,2,3,4,5]
        output = 4
        self.assertEqual(
            self.solution.findLengthOfLCIS(nums),
            output
        )

if __name__ == '__main__':
    unittest.main()

