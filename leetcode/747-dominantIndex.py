# 747-dominantIndex.py

# 747. Largest Number At Least Twice of Others

# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

# Example 1:

# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


# Example 2:

# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


# Note:

# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # loop through keeping track of the largest element
        # and the second largest element

        largest = 0
        largest_idx = 0
        second_largest = 0

        for idx, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                largest_idx = idx
            elif num > second_largest:
                second_largest = num

        if largest >= (second_largest * 2):
            return largest_idx
        else:
            return -1

if __name__ == '__main__':
    solution = Solution()


    print("Example 1 should be 1:", solution.dominantIndex([3, 6, 1, 0]))
    print("Example 2 should be -1:", solution.dominantIndex([1, 2, 3, 4]))