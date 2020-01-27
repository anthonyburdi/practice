# Jumping_on_the_Clouds_EASY.py

# Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

# For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .

# Function Description

# Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

# jumpingOnClouds has the following parameter(s):

# c: an array of binary integers
# Input Format

# The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

# Constraints

# Output Format

# Print the minimum number of jumps needed to win the game.

# Sample Input 0

# 7
# 0 0 1 0 0 1 0
# Sample Output 0

# 4
# Explanation 0:
# Emma must avoid  and . She can win the game with a minimum of  jumps:

# jump(2).png

# Sample Input 1

# 6
# 0 0 0 0 1 0
# Sample Output 1

# 3
# Explanation 1:
# The only thundercloud to avoid is . Emma can win the game in  jumps:

# jump(5).png


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # Assumptions
    # c fits on a single machine
    # always solvable (see question)
    # c is always 0 or 1 and 2 <= len <= 100
    # first and last digits are always 0

    # Approach
    # Iterate through the clouds.
    # if the next cloud is a 1, then add 1 jump and then skip the index forward
    # two spaces.
    # if the next cloud is a 0, check the one after that. If it is also a 0
    # then add 1 jump and skip the index forward two spaces
    # If the one after the next cloud is a 1 then skip the index forward one
    # space and add one jump
    # if our current index is the last item in the array then exit
    # if our current index is the pentultimate, then only check the next cloud
    # not the one after that.

    # Complexity
    # Time: O(N) since we check all clouds
    # Space: O(1) since we only keep pointers

    # Potential Improvements
    # Maybe we can use a bit of math? Although the ordering matters.
    # E.g. can we sum c and compare it to it's length? But that is also
    # O(N) anyway since we have to sum each item.
    # This might work in this particular case but since it has the same
    # complexity even if it does we'll skip it.

    # Edge Cases
    # only two clouds (both have to be 0)

    # Take care of edge case
    if len(c) == 2:
        return 1

    jumps = 0
    i = 0
    # check up to but not including the pentultimate cloud, e.g.:
    # c = 0, 0, 0, 1, 0
    # i = 0, 1, 2, 3, 4
    # len(c) = 5
    # while i < 3 so i = 3 when loop ends but last run it was 2

    while i < len(c) - 2:

        # if the next cloud is unsafe, jump over it
        if c[i + 1] == 1:
            jumps += 1
            i += 2
            continue

        # if the next two clouds are safe jump two
        if c[i + 1] == 0:
            if c[i + 2] == 0:
                jumps += 1
                i += 2
                continue

        # if the next is safe but the one after is not then jump one
            if c[i + 2] == 1:
                jumps += 1
                i += 1


    # check the pentultimate if we are not at the end
    if i < len(c) - 1:
        if c[i] == 0:
            jumps += 1

    return jumps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # c = list(map(int, input().rstrip().split()))

    # result = jumpingOnClouds(c)

    # fptr.write(str(result) + '\n')

    # fptr.close()


# failing case:
# 100
# 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0

# answer 53
# Was missing the continue statements

