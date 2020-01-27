# Arrays_Left_Rotation_EASY.py

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

# Function Description

# Complete the function rotLeft in the editor below. It should return the resulting array of integers.

# rotLeft has the following parameter(s):

# An array of integers .
# An integer , the number of rotations.
# Input Format

# The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

# Sample Input

# 5 4
# 1 2 3 4 5
# Sample Output

# 5 1 2 3 4
# Explanation

# When we perform  left rotations, the array undergoes the following sequence of changes:

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    # Assumptions
    # a and d are or contain integers
    # d is positive > 1
    # d is less than n (we can do more than n, just take the mod: d % len(n)
    # so that we only rotate the remainder of d // len(n))
    # items in a are positive integers
    # some of these assumptions are unnecessary but given by the problem statement

    # Approach
    # 1. pop(0) and append each digit d times. This is O(N) for the popleft
    # if using on a normal python list.
    # 2. use dequeue to popleft and append. This is O(1) for both the popleft
    # and the append. But we do this for O(d) elements so worst case is O(n).
    # 3. for each d: remove the first element and store it. move each element
    # after one space to the left, then insert the stored element at the end
    # of the list. Use pointers and a for loop. This is also O(N) and similar
    # if not exactly the same depending on python's implementation to the
    # first approach.
    # 4. If we can use extra space, we can just slice the list at element d.
    # We create a new list starting from d and one from 0 up to d - 1
    # we return these two lists concatenated together.
    # This solution is O(n) since we do O(k) on each slice.

    # Let's choose approach # 2 if we can import dequeue since it is in place
    # actually we do need to create a dequeue object so it is not really
    # in place. Creating the dequeue object is also O(n) so it is the same
    # as option 4.
    # I changed my mind - let's go with option 4 since it is the simplest
    # to understand.

    # Complexity
    # Approach 4
    # Time: O(n) since we do a slice on both halves of the array at O(k) each
    # Space: O(n) since we store the halves before joining them back together

    # Potential Improvements
    # I can't think of any, all tradeoffs are covered in the Approach section.

    # Edge Cases
    # None that are not already covered in the problem Constraints

    return a[d:] + a[:d]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
