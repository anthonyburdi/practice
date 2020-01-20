# 34-Find_First_and_Last_Position_of_Element_in_Sorted_Array_MEDIUM.py

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Assumptions
        # given integers sorted in ascending order
        # list of integers fits in memory on a single machine

        # Approach
        # Some version of binary search. But when we find the item, continue checking
        # to the left until we find the min and then to the right for the max
        # We can maybe do this part just by iterating? Though in the worst case
        # that would be O(N) if all items are the same.
        # Let's look at an example
        # [5,7,7,8,8,10]
        # left = 0; right = 5; mid = left + (right - left) // 2 = 2
        # target (8) > nums[mid] (7) so left = mid
        # left = 2; right = 5; mid = 3
        # target (8) == nums[mid] (8) so now we've found one of the targets
        # we could do brute force here and go left and right from min until we find
        # a different number, one item at a time
        # or
        # set our output [min, max] = [mid, mid]
        # then binary search outward to find the min and max
        # so min_search looks to the left of mid between the beginning and mid - 1
        # if it finds the target, then it sets the new minimum and calls itself again
        # on the part that is left between left and new minimum
        # if it does not find the target then we have found our minimum
        # we do the same with the upper range

        # Complexity
        # Time: O(log n) since we halve the search space each iteration
        # we do several searches, but it is still O(log n)

        # Potential improvements
        # I can't think of any

        """Find start and end location of target in sorted array of ints."""

        # Optimization: check if all = target
        if nums and (nums[0] == target) and (nums[-1] == target):
            return [0, len(nums) - 1]

        first_pass = self.binarySearch(nums, target, 0, len(nums) - 1)
        min_max = [first_pass, first_pass]
        if first_pass == -1:
            return min_max

        # left search
        left = 0
        right = min_max[0] - 1
        while True:
            min_candidate = self.binarySearch(nums, target, left, right)
            if min_candidate == -1:
                break
            if min_candidate < min_max[0]:
                min_max[0] = min_candidate
                right = min_candidate - 1

        # right search
        left = min_max[1] + 1
        right = len(nums) - 1
        while True:
            max_candidate = self.binarySearch(nums, target, left, right)
            if max_candidate == -1:
                break
            if max_candidate > min_max[1]:
                min_max[1] = max_candidate
                left = max_candidate + 1

        return min_max

    def binarySearch(
        self, nums: List[int], target: int, left: int, right: int
    ) -> int:
        """Return index of target using binary search."""

        if not nums or target == None:
            return -1
        if (left < 0) or (right < 0) or (right > len(nums) - 1):
            return -1

        if left == None or left < 0:
            left = 0
        if right == None or right < 0:
            right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        return -1


import unittest

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.nums = [5,7,7,8,8,10]
        self.target1 = 8
        self.target2 = 6

    def test_example_1(self):
        self.assertIn(
            self.solution.binarySearch(self.nums, self.target1, 0, 5),
            [3, 4]
        )

    def test_example_1a(self):
        self.assertEqual(
            self.solution.binarySearch(self.nums, self.target1, 4, 5),
            4
        )
        self.assertEqual(
            self.solution.binarySearch(self.nums, self.target1, 0, 3),
            3
        )

    def test_empty_nums(self):
        self.assertEqual(
            self.solution.binarySearch([], self.target1, 0, 5),
            -1
        )

    def test_out_of_bounds(self):
        self.assertEqual(
            self.solution.binarySearch(self.nums, self.target1, -5, 2),
            -1
        )
        self.assertEqual(
            self.solution.binarySearch(self.nums, self.target1, 0, 25),
            -1
        )
        self.assertEqual(
            self.solution.binarySearch(self.nums, self.target1, -25, 25),
            -1
        )

    def test_small_nums_1(self):
        self.assertEqual(
            self.solution.binarySearch([1], 1, 0, 0),
            0
        )

    def test_small_nums_2(self):
        self.assertEqual(
            self.solution.binarySearch([1], 2, 0, 0),
            -1
        )

    def test_last_element_is_target(self):
        self.assertEqual(
            self.solution.binarySearch([0,1,2], 2, 2, 2),
            2
        )

    def test_last_element_is_not_target(self):
        self.assertEqual(
            self.solution.binarySearch([0,1,2], 3, 2, 2),
            -1
        )
        self.assertEqual(
            self.solution.binarySearch([0,1,2], -5, 2, 2),
            -1
        )

    def test_first_element_is_target(self):
        self.assertIn(
            self.solution.binarySearch([0,0,0,1,2,3], 0, 0, 5),
            [0, 1, 2]
        )
        self.assertIn(
            self.solution.binarySearch([-1,-1,-1,1,2,3], -1, 0, 5),
            [0, 1, 2]
        )

    def test_target_is_0(self):
        self.assertIn(
            self.solution.binarySearch([-5,-2,-1,0,0,0,1,2,3], 0, 0, 8),
            [3, 4, 5]
        )

    def test_target_is_minus_1(self):
        self.assertIn(
            self.solution.binarySearch([-5,-2,-1,-1,-1,0,0,0,1,2,3], -1, 0, 10),
            [2, 3, 4]
        )

class TestSearchRange(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.nums = [5,7,7,8,8,10]
        self.target1 = 8
        self.target2 = 6

    # Example 1:

    # Input: nums = [5,7,7,8,8,10], target = 8
    # Output: [3,4]

    def test_example_1(self):
        output = [3, 4]
        self.assertEqual(
            self.solution.searchRange(self.nums, self.target1),
            output
        )


    # Example 2:

    # Input: nums = [5,7,7,8,8,10], target = 6
    # Output: [-1,-1]

    def test_example_2(self):
        output = [-1,-1]
        self.assertEqual(
            self.solution.searchRange(self.nums, self.target2),
            output
        )


    def test_empty_nums(self):
        output = [-1,-1]
        self.assertEqual(
            self.solution.searchRange([], self.target2),
            output
        )


    def test_empty_target(self):
        output = [-1,-1]
        self.assertEqual(
            self.solution.searchRange(self.nums, None),
            output
        )


    def test_all_target(self):
        nums = [1,1,1,1,1,1,1,1,1,1]
        target = 1
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [0, 9]
        )


    def test_mostly_target(self):
        nums = [0,1,1,1,1,1,1,1,1,1,1,2]
        target = 1
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [1, 10]
        )

    def test_one_digit_on_either_end_of_target(self):
        nums = [0,1,2]
        target = 1
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [1, 1]
        )

    # BUGFIX
    # Example:
    # nums = [0,1,2]
    # target = 1
    # first_pass = 1; min_max = [1, 1]
    # left = 0; right = 1 - 1 = 0; mid = 0
    # Maybe this is why it is getting stuck since left, right, mid = 0?
    # min_candidate = -1; break
    # left = 1 + 1 = 2; right = 3 - 1 = 2; mid = 2
    # max_candidate = -1; break
    # return min_max = [1, 1] which is the right answer....
    # I'm stumped
    # will try pdb

    # Looks like here is the problem:
    # if not left:
    #     left = 0
    # if not right:
    #     right = len(nums) - 1

    # Because left or right = 0 is setting the defaults and forcing an infinite
    # loop since we are constantly looking at the whole array.
    # I need to change this to look for None instead of not.... or negative.

    # Changed to:
    # if left == None or left < 0:
    #     left = 0
    # if right == None or right < 0:
    #     right = len(nums) - 1


    def test_two_digits_on_either_end_of_target(self):
        nums = [0,0,1,2,2]
        target = 1
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [2, 2]
        )


    def test_negative_numbers_only(self):
        nums = [-10,-10,-8,-4,-4,-4,-4,-4,-1,-1,-1,-1,-1]
        target = -4
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [3, 7]
        )
        target = -1
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [8, 12]
        )
        target = -10
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [0, 1]
        )


    def test_target_at_beginning(self):
        nums = [0,0,0,1,2,3]
        target = 0
        self.assertEqual(
            self.solution.searchRange(nums, target),
            [0, 2]
        )

    # BUGFIX
    # Example:
    # nums = [0,0,0,1,2,3]
    # target = 0
    # answer = [0, 2]

    # first_pass = -1
    # why is first_pass = -1?
    # This issue seems to be in binarySearch...
    # if not nums or not target:
    #     return -1
    # if (left < 0) or (right < 0) or (right > len(nums) - 1):
    #     return -1

    # This line appears to be the issue, since target is 0:
    # if not nums or not target:


if __name__ == '__main__':
    unittest.main()

    # Debug:
    # nums = [0,1,2]
    # target = 1
    # solution = Solution()
    # print("Should be [1, 1]:", solution.searchRange(nums, target))



