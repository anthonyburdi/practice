# Sorting_Bubble_Sort.py

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

# Consider the following version of Bubble Sort:

# for (int i = 0; i < n; i++) {

#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#         }
#     }

# }
# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.
# Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

# For example, given a worst-case but small array to sort:  we go through the following steps:

# swap    a
# 0       [6,4,1]
# 1       [4,6,1]
# 2       [4,1,6]
# 3       [1,4,6]
# It took  swaps to sort the array. Output would be

# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 6
# Function Description

# Complete the function countSwaps in the editor below. It should print the three lines required, then return.

# countSwaps has the following parameter(s):

# a: an array of integers .
# Input Format

# The first line contains an integer, , the size of the array .
# The second line contains  space-separated integers .

# Constraints

# Output Format

# You must print the following three lines of output:

# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.
# Sample Input 0

# 3
# 1 2 3
# Sample Output 0

# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3
# Explanation 0
# The array is already sorted, so  swaps take place and we print the necessary three lines of output shown above.

# Sample Input 1

# 3
# 3 2 1
# Sample Output 1

# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
# Explanation 1
# The array is not sorted, and its initial values are: . The following  swaps take place:

# At this point the array is sorted and we print the necessary three lines of output shown above.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    # Assumptions
    # Covered in the constraints
    # Assume slow bubble sort runtime is OK.

    # Approach, Complexity, Tradeoffs
    # implement bubble sort like in the example
    # during each swap, increment a counter
    # O(N^2) runtime O(1) space

    # Potential improvements

    # Edge Cases
    # n = 0 or 1 (Constraints handle this)

    def swap(arr, index_1: int, index_2: int) -> None:
        """Swap two items in arr given their indices, in place."""
        temp = arr[index_1]
        arr[index_1] = arr[index_2]
        arr[index_2] = temp

    # Counter
    swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                # swap(a, j, j + 1)
                # temp = a[j]
                # a[j] = a[j+1]
                # a[j+1] = temp
                a[j], a[j+1] = a[j+1], a[j]

                swaps += 1

    print("Array is sorted in {} swaps.".format(str(swaps)))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))




if __name__ == '__main__':
    # n = int(input())

    # a = list(map(int, input().rstrip().split()))

    # countSwaps(a)

    a = [3,2,1]
    countSwaps(a)

