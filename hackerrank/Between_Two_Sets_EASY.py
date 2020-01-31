# Between_Two_Sets_EASY.py

# https://www.hackerrank.com/challenges/between-two-sets/problem

# You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

# For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value. Similarly, ,  and , .

# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):

# a: an array of integers
# b: an array of integers
# Input Format

# The first line contains two space-separated integers,  and , the number of elements in array  and the number of elements in array .
# The second line contains  distinct space-separated integers describing  where .
# The third line contains  distinct space-separated integers describing  where .

# Constraints

# Output Format

# Print the number of integers that are considered to be between  and .

# Sample Input

# 2 3
# 2 4
# 16 32 96
# Sample Output

# 3
# Explanation

# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.

# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Assumptions
    # Data fits on a single machine
    # All data are positive integers
    # integers could not be in sorted order (though they are in the examples)

    # Approach, Complexity, Tradeoffs and Potential Improvements
    # Try numbers between the min of a and min of b
    # only try numbers that are a multiple of the items in a
    # for example try all the items in a. Then try a[0] * 2 then * 3 until
    # we meet or exceed the min of b
    # then try a[1] * 2, then * 3 and so on until we meet or exceed min(b)
    # and so on for each member of a
    # I'm sure we can get rid of some more of these cases mathematically.
    # Time complexity is O(a + b) for finding the min. Then for finding the
    # cases it's a bit tougher to figure out.
    # Space complexity is O(1) except for the storage of the interim solution
    # so O(a + b) at least if there are a lot of solutions.
    #

    # Edge Cases
    # single item lists
    # overlapping lists

    def check_if_between(a, b, num) -> bool:
        """Check if a number is between two sets as defined in the prob."""
        for item_a in a:
            if num % item_a != 0:
                return False

        for item_b in b:
            if item_b % num != 0:
                return False

        return True

    solutions = set()

    min_b = min(b)
    for item in a:
        candidate = None
        multiplier = 1
        while candidate == None or candidate <= min_b:
            candidate = item * multiplier
            if check_if_between(a, b, candidate):
                solutions.add(candidate)
            multiplier += 1

    return len(solutions)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
