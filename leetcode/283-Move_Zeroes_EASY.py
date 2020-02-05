# 283-Move_Zeroes_EASY.py

# https://leetcode.com/problems/move-zeroes/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Assumptions
# nums fits on a single computer
# nums contains only integers
# negative numbers are treated the same as positive

# Approach Complexity Tradeoffs Improvements
# 1. Two pointers. One for 0's and one for non-0's.
# If we hit a zero, swap it with the next non zero. If non zero hits the end
# of the array we are done
# O(N) time and constant space

# 2. pop zeroes and append them
# This is simpler but popping toward the front of the list
# is O(N). Then we also need to check whether there are any non zero items
# otherwise we'll loop forever.

# Edge Cases
# empty array, single item, no zeroes, only zeroes

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        while i < len(nums) and not all(j == 0 for j in nums[i:]):
            if nums[i] == 0:
                zero_to_move = nums.pop(i)
                nums.append(zero_to_move)
            else:
                i += 1

        # zero = 0
        # nonzero = 0

        # while nonzero < len(nums) and zero < len(nums):
        #     if nums[zero] != 0:
        #         zero += 1

        #     if nums[nonzero] == 0:
        #         nonzero += 1

        #     if nums[zero] == 0 and nums[nonzero] != 0 and zero < nonzero:
        #         nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
        #         zero, nonzero = nonzero, zero
        #     else:
        #         zero += 1
        #         nonzero += 1




import unittest

class TestMoveZeroes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_failing_example(self):

        nums = [0,-1,0,0,0,-5,-132,13,-34,335,1,0,-45]
        self.solution.moveZeroes(nums)

        self.assertEqual(
            [-1,-5,-132,13,-34,335,1,-45,0,0,0,0,0],
            # self.solution.moveZeroes(nums)
            nums
        )



    def test_other_examples(self):
        pass
        # INPUT
        # [0,1,0,3,12]
        # [1]
        # [0]
        # []
        # [0,-1,0,0,0,-5,-132,13,-34,335,1,0,-45]

        # EXPECTED OUTPUT
        # [1,3,12,0,0]
        # [1]
        # [0]
        # []
        # [-1,-5,-132,13,-34,335,1,-45,0,0,0,0,0]



if __name__ == '__main__':
    unittest.main()

