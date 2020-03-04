# Problem-79-[Medium].py

# This problem was asked by Facebook.

# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.


# Assumptions
# integers can be negative or 0

# Approach
# loop through array checking previous and next values (careful at ends)
# if a value needs to be modified (bigger than next or less than previous)
# then we increment a modifications counter
# if this modifications counter is >1 at any point then return False
# O(N) time  and O(1) space

# Does this work? Let's check some examples
# [-5, 2, 13, 0, 14, 92, 123, 4] (False)
# first modify 0 bc less than 13 to be 13 (keep track of change in hashmap)
# then ok till 4 but already modified so false

# [-8, 12, -7, -6, -1] (True)
# first modify 12 to be -8 since it is larger than -8
# then continue and no further edits

# [2, 1, 3]
# increase 1 to 2

# [1, 3, 2]
# increase 2 to 3

# [2, 3, 1]
# increase 1 to 3


# [1, 2, 3, 4, 10, 5, 7]
# Doesn't work here bc we would change 5 to 10 but we could have changed
# 10 to 4 or 5
# Should we change it to the minimum of it's neighbors? That would cover
# this case


# Edge Cases
# nums go up then down then back up but not to highest level
# edit at beginning or end
# len 0

from typing import List

def check_non_decreasing(arr: List[int]) -> bool:
    """Can arr become non-decreasing by modifying at most 1 element?."""

    # check to make sure not empty or small
    if len(arr) <= 1:
        return True

    modifications = {}
    # Check first digit, reduce to 2nd digit if larger
    if arr[0] > arr[1]:
        modifications[0] = arr[1]

    # check middle digits
    i = 1
    while i < len(arr) - 1:

        # not all of these need to be checked for modifications
        # next_val = modifications.get(i + 1, arr[i + 1])
        next_val = arr[i + 1]
        prev_val = modifications.get(i - 1, arr[i - 1])
        # curr_val = modifications.get(i, arr[i])
        curr_val = arr[i]

        # Set curr val to min of neighbors if not correct
        if curr_val < prev_val or curr_val > next_val:
            modifications[i] = min(prev_val, next_val)


        if len(modifications) > 1:
            return False

        i += 1

    # check last digit

    return True


import unittest

class TestCheckNonDecreasing(unittest.TestCase):

    def test_given_examples(self):

        self.assertTrue(check_non_decreasing([10, 5, 7]))
        self.assertFalse(check_non_decreasing([10, 5, 1]))


    def test_my_examples(self):

        self.assertTrue(check_non_decreasing([1, 2, 3, 4, 10, 5, 7]))
        self.assertFalse(check_non_decreasing([-5, 2, 13, 0, 14, 92, 123, 4]))


if __name__ == '__main__':
    unittest.main()

















