# 448-Find_All_Numbers_Disappeared_in_an_Array_EASY.py

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # We can use hash sets for a simple solution
        # first we convert the list to a hash set and create one for [1,n]
        # This step is O(N) since we have to look at each item to create the set
        # then we take the difference and convert it back to a list
        # this takes O(N) extra space
        input_set = set(nums)
        full_set = set(list(range(1,len(nums)+1)))
        return sorted(list(full_set - input_set))

        # for an in-place and O(N) solution
        # ....


import unittest

class TestFindDisappearedNumbers(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        input_list = [4,3,2,7,8,2,3,1]
        output_list = [5,6]

        self.assertEqual(
            self.solution.findDisappearedNumbers(input_list),
            output_list
        )

    def test_example_2(self):
        input_list = [1,1]
        output_list = [2]
        self.assertEqual(
            self.solution.findDisappearedNumbers(input_list),
            output_list
        )


if __name__ == '__main__':
    unittest.main()

