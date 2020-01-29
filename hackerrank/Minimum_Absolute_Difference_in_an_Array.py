# Minimum_Absolute_Difference_in_an_Array.py

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

# Consider an array of integers, . We define the absolute difference between two elements,  and  (where ), to be the absolute value of .

# Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array  we can create  pairs of numbers:  and . The absolute differences for these pairs are ,  and . The minimum absolute difference is .

# Function Description

# Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

# minimumAbsoluteDifference has the following parameter(s):

# n: an integer that represents the length of arr
# arr: an array of integers
# Input Format

# The first line contains a single integer , the size of .
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Print the minimum absolute difference between any two elements in the array.

# Sample Input 0

# 3
# 3 -7 0
# Sample Output 0

# 3
# Explanation 0

# With  integers in our array, we have three possible pairs: , , and . The absolute values of the differences between these pairs are as follows:

# Notice that if we were to switch the order of the numbers in these pairs, the resulting absolute values would still be the same. The smallest of these possible absolute differences is .

# Sample Input 1

# 10
# -59 -36 -13 1 -53 -92 -2 -96 -54 75
# Sample Output 1

# 1
# Explanation 1

# The smallest absolute difference is .

# Sample Input 2

# 5
# 1 -3 71 68 17
# Sample Output 2

# 3
# Explanation 2

# The minimum absolute difference is .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    # Assumptions
    # We can sort within time limit

    # Approach, Complexity & Tradeoffs
    # Sort the array and find min of diff between successive elements
    # Time: NlogN for sort and N for search
    # Space: O(1) if sort in place otherwise O(N)

    # Potential Improvement
    # Maybe there is a way to get to O(N)?

    # Edge Cases
    # Large arrays, small arrays

    arr_sorted = sorted(arr)
    min_abs_diff = None
    i = 0
    while i < (len(arr_sorted) - 1):
        abs_diff = abs(arr_sorted[i] - arr_sorted[i+1])
        if min_abs_diff is None or abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
        i += 1

    return min_abs_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()





























