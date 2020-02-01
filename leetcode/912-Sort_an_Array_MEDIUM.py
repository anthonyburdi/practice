# 912-Sort_an_Array_MEDIUM.py

# https://leetcode.com/problems/sort-an-array/

# Given an array of integers nums, sort the array in ascending order.



# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]


# Constraints:

# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000

# Assumptions
# See constraints
# Nums are integers
# integers can include 0 and negative nums
# nums can include duplicates

# Approach, Complexity, Tradeoffs, Potential Improvements
# Merge sort recursive or iterative, quicksort
# Basically any of the sorting algorithms
# Since we just implemented mergesort recursively let's do that
# First split the array up in half until we have 0-1 nodes
# then merge the resulting arrays back together by iterating through them
# both and picking the smaller or equal item at each step
# Complexity is O(NlogN) since the split takes logN time and the merge O(N)
# Space complexity is O(N) since we store a lot of intermediate data
# at most the full array.
# We could also do this in place if we needed to using pointers.

# Edge Cases
# empty or single item

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)


    def merge(self, left: List[int], right: List[int]) -> List[int]:

        merged = []

        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # add rest of items if any are left
        if i < len(left):
            merged += left[i:]
        elif j < len(right):
            merged += right[j:]

        return merged



import unittest

class TestSortArray(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_example_1(self):
        nums = [5,2,3,1]
        output = [1,2,3,5]
        self.assertEqual(
            self.solution.sortArray(nums),
            output
        )

    def test_example_2(self):
        nums = [5,1,1,2,0,0]
        output = [0,0,1,1,2,5]
        self.assertEqual(
            self.solution.sortArray(nums),
            output
        )

    def test_random_example(self):
        max_len = 50000
        # intervals are inclusive
        start_interval = -50000
        end_interval = 50000

        import random
        rand_list = [
            random.randint(start_interval, end_interval)
            for _ in range(max_len)
        ]

        sorted_rand_list = sorted(rand_list)

        self.assertEqual(self.solution.sortArray(rand_list), sorted_rand_list)


if __name__ == '__main__':
    unittest.main()

