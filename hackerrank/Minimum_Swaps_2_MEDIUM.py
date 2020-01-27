# Minimum_Swaps_2_MEDIUM.py

# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

# For example, given the array  we perform the following steps:

# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took  swaps to sort the array.

# Function Description

# Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.

# minimumSwaps has the following parameter(s):

# arr: an unordered array of integers
# Input Format

# The first line contains an integer, , the size of .
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Return the minimum number of swaps to sort the given array.

# Sample Input 0

# 4
# 4 3 1 2
# Sample Output 0

# 3
# Explanation 0

# Given array
# After swapping  we get
# After swapping  we get
# After swapping  we get
# So, we need a minimum of  swaps to sort the array in ascending order.

# Sample Input 1

# 5
# 2 3 4 1 5
# Sample Output 1

# 3
# Explanation 1

# Given array
# After swapping  we get
# After swapping  we get
# After swapping  we get
# So, we need a minimum of  swaps to sort the array in ascending order.

# Sample Input 2

# 7
# 1 3 5 2 4 6 7
# Sample Output 2

# 3
# Explanation 2

# Given array
# After swapping  we get
# After swapping  we get
# After swapping  we get
# So, we need a minimum of  swaps to sort the array in ascending order.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    # Assumptions
    # return output (rather than print)
    # data small enough to handle on a single computer
    # integers start with 1 and end with len(arr)

    # Approach, Complexity, Tradeoffs
    # It looks like we can iterate through and swap each item with where it
    # should go (if not already in it's place). This gives the same answers
    # as in the example, even with different swaps. I tried to think if there
    # was maybe a mathematical relationship f(len(q)) = min_swaps but if so
    # it is likely only an upper bound. Consider the case where only two items
    # are out of place compared to when the array is sorted in descending order
    # These give different min_swaps for sufficient sized arrays.
    # So we iterate through, keeping track of pointer + 1 and comparing that
    # to the item in the current space. If they are equal then increment
    # the pointer. If not then store the value and move the value in the
    # current digit - 1 indexed spot to the current spot. Then place the
    # stored value in it's index = (current_digit - 1) spot.
    # For each swap increment a swap_counter

    # Time complexity: O(N) where N is length of q. We hit at maximum all
    # items in the array. The swap is O(1) since it is just an insertion
    # and access by index.
    # Space complexity: O(1) since we do this in place with only pointers and
    # temp storage of a single item & swap_counter.

    # Potential Improvements
    # I can't think of any.

    # Edge Cases
    # n = 1 = 0 swaps
    # n = 2 (maybe not edge case). Either 0 or 1 swaps. Actually not edge case
    # others are contained in problem constraints.

    # Handle edge cases
    if len(arr) == 1:
        return 0

    swap_counter = 0
    i = 0

    while i < len(arr):
        if arr[i] == i + 1:
            i += 1
        else:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swap_counter += 1

    return swap_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

