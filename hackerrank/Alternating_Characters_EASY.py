# Alternating_Characters_EASY.py

# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

# You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

# Your task is to find the minimum number of required deletions.

# For example, given the string , remove an  at positions  and  to make  in  deletions.

# Function Description

# Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

# alternatingCharacters has the following parameter(s):

# s: a string
# Input Format

# The first line contains an integer , the number of queries.
# The next  lines each contain a string .

# Constraints

# Each string  will consist only of characters  and
# Output Format

# For each query, print the minimum number of deletions required on a new line.

# Sample Input

# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB
# Sample Output

# 3
# 4
# 0
# 0
# 4
# Explanation

# The characters marked red are the ones that can be deleted so that the string doesn't have matching consecutive characters.

# image


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    # Assumptions
    # only chars A and B
    # string fits on a single computer

    # Approach, Complexity, Tradeoffs, Potential Improvements
    # since python strings are immutable, let's first convert to a char array
    # for O(N) time. Then we can pop out the elements that match their
    # preceding element for O(N) time. Afterwards we can join back together
    # Actually that is O(N) space. We can do a little better by
    # creating the char array of the return string as we iterate through
    # Still O(N) In time and space but a little better.

    # Whoops - we just need to return the number of deletions
    # So we are still at O(N) time but O(1) space

    # Edge Cases
    # All the same letter
    # single letter
    # empty string

    # return_array = []
    prev_char = ''
    i = 0
    num_deletions = 0

    while i < len(s):
        if s[i] != prev_char:
            # return_array.append(s[i])
            prev_char = s[i]
        else:
            num_deletions += 1
        i += 1

    # return "".join(return_array)
    return num_deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
