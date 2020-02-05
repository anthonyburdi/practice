# 75-Sort_Colors_MEDIUM.py

# https://leetcode.com/problems/sort-colors/

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Approach:
        # traverse pointers until they hit the first instance of their color
        # or hit the end of the list
        # Start with red and white
        # if the red pointer is past the white then swap and start them
        # both again at the lower index
        # then do the same for the white and blue
        # O(N) approximately since we pass once (with some backtracking)

        if len(nums) <= 1:
            return

        # initialize pointers
        r = w = b = 0

        while True:
            # find red
            while True:
                if r >= len(nums) or nums[r] == 0:
                    break
                else:
                    r += 1
            # find white
            while True:
                if w >= len(nums) or nums[w] == 1:
                    break
                else:
                    w += 1
            # find blue
            while True:
                if b >= len(nums) or nums[b] == 2:
                    break
                else:
                    b += 1

            # Swap red nodes if out of place
            if r < len(nums):
                if (r > w or r > b) and w < b:
                    nums[r], nums[w] = nums[w], nums[r]
                    r = w + 1
                    # leave w alone so we can find the next w
                    continue

                elif (r > w or r > b) and b < w:
                    nums[r], nums[b] = nums[b], nums[r]
                    r = b + 1 # next
                    # leave b alone so we can find the next b
                    continue
                else:
                    r += 1
                    continue

            # Swap white nodes if out of place
            if w < len(nums):
                if w > b:
                    nums[w], nums[b] = nums[b], nums[w]
                    w = b + 1
                else:
                    w += 1

            if w >= len(nums) and r >= len(nums):
                break


import unittest

class TestSortColors(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):
        i = [2,0,2,1,1,0]
        o = [0,0,1,1,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)


    def test_edge_cases(self):
        i = [1]
        o = [1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = []
        o = []
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [1,2,2,1,1]
        o = [1,1,1,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [0,2,2,0,0]
        o = [0,0,0,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [2,0,0,0,2]
        o = [0,0,0,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [1,0,0,0,1]
        o = [0,0,0,1,1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [0,0,1,1,0]
        o = [0,0,0,1,1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [1,0,0,1,1]
        o = [0,0,1,1,1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [0,0,0,0,0]
        o = [0,0,0,0,0]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [1,1,1,1,1]
        o = [1,1,1,1,1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [2,2,2,2,2]
        o = [2,2,2,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)


    def test_leetcode_wrong_answer(self):

        i = [0,1,0]
        o = [0,0,1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [0,2,0]
        o = [0,0,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [1,0,1]
        o = [0,1,1]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [1,2,1]
        o = [1,1,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [2,0,2]
        o = [0,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)

        i = [2,1,2]
        o = [1,2,2]
        self.solution.sortColors(i)
        self.assertEqual(i,o)


if __name__ == '__main__':
    unittest.main()















