# 665-Non-decreasing_Array_EASY.py

# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].

# Assumptions:
# negative and 0 ARE NOT included in n integers (see Note in problem statement)
# [] blank array should return True (checked on Leetcode)
# [1] single item array should return True (checked on Leetcode)
# All the data fits in memory of a single machine
# non-decreasing includes repeated digits e.g. [1,2,2,3,7,5] is still True
# since we can modify the 7 to a 4 (or 3 or 5). The 2's don't matter, since
# although they are not "increasing" they are still non-decreasing.

# Approach:
# iterate through the array, for the first instance of a decreasing integer
# change it to non-decreasing if possible and keep going. If this happens
# again, return False since we can modify at most 1 element
# If we find an element bigger than the following element

# Round 2: we do have to make the modification I think then re-check
# in order to fix issues like this one [3,4,2,3] should be false bc
# we would modify the 2 to a 4, making the 3 at the end another modification
# that is needed (whereas if left as a 2 it wouldn't need to be modified)

# Round 3: I think we have to look at the previous digit as well...
# e.g. [2,3,3,2,4] needs to be True since we can modify the 2 to a 3
# let's look at all the cases of this and see if we can find a pattern
# TODO: ___________________________________________________________________

# cases
# 1. decrease the current digit to be equal to the next digit
# 2. increase the next digit to be equal to the current digit


# Time and Space Complexity:
# O(N) time complexity since we visit each integer, and modify the array
# in-place
# O(1) space complexity since we just add a few variables

# Potential Improvements:
# Maybe we can break sooner in some cases to return False?
# We can change max_modifications to allow more modifications

# The current solution can definitely be improved. We could not make so many
# list copies for example.


from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """Can we modify at most 1 element to get non-decreasing array?"""

        nums_copy_1 = nums.copy()
        nums_copy_2 = nums.copy()

        decrease_current = None
        increase_next = None
        # cases
        # 1. decrease the current digit to be equal to the next digit

        max_modifications = 1
        modifications = 0

        i = 0
        while i  < (len(nums_copy_1) - 1):
            if nums_copy_1[i] > nums_copy_1[i + 1]:
                modifications += 1
                # decrease the current digit to be equal to the next digit
                nums_copy_1[i] = nums_copy_1[i + 1]
                # Restart the check at item 0 with modification
                i = -1

            if modifications > max_modifications:
                decrease_current = False
                break

            i += 1

        if decrease_current == None:
            decrease_current = True


        # 2. increase the next digit to be equal to the current digit
        max_modifications = 1
        modifications = 0

        i = 0
        while i  < (len(nums_copy_2) - 1):
            if nums_copy_2[i] > nums_copy_2[i + 1]:
                modifications += 1
                # increase the next digit to be equal to the current digit
                nums_copy_2[i + 1] = nums_copy_2[i]
                # Restart the check at item 0 with modification
                i = -1

            if modifications > max_modifications:
                increase_next = False
                break

            i += 1

        if increase_next == None:
            increase_next = True

        return  decrease_current or increase_next


# ------------------------------------------------------------------------------
# Test cases
# ------------------------------------------------------------------------------

# Given examples
# one item at the end of the array
# second item at the end of the array
# many modifications needed
# small given arrays
# increasing and then reducing before increasing again (but not to orig level)
# e.g. [3,4,2,3]


# [1,2,2,3,7,5] = True
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False

import unittest

class TestCheckPossibility(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # Given examples

    def test_example_1(self):
        # Example 1:
        # Input: [4,2,3]
        # Output: True
        input_nums = [4,2,3]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    def test_example_2(self):
        # Example 2:
        # Input: [4,2,1]
        # Output: False
        input_nums = [4,2,1]
        expected_output = False
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    # equal numbers throughout array
    def test_equal_numbers_in_array(self):
        input_nums = [1,2,2,3,7,5]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )
        input_nums = [1,2,2,3,4,5]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    # one item at the end of the array
    def test_one_item_at_end_of_array(self):
        input_nums = [0,2,3,5,9,6]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    # second item at the end of the array
    def test_second_item_at_end_of_array(self):
        input_nums = [0,2,6,5,9,6]
        expected_output = False
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    # many modifications needed
    def test_many_modifications_needed(self):
        input_nums = [0,1,2,1,2,1,2,1,2,1,2,99,100,99,21,19,37,29,10]
        expected_output = False
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    # small given arrays (len 0 and 1)
    def test_small_arrays_1(self):
        input_nums = []
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    def test_small_arrays_2(self):
        input_nums = [1]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )
        input_nums = [9999]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    def test_increase_then_decrease_and_increase_again(self):
        input_nums = [3,4,2,3]
        expected_output = False
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )

    def test_testcase_from_leetcode(self):
        input_nums = [2,3,3,2,4]
        expected_output = True
        self.assertEqual(
            self.solution.checkPossibility(input_nums),
            expected_output
        )


if __name__ == '__main__':
    unittest.main()


