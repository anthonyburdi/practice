# Two_Strings_EASY.py

# https://www.hackerrank.com/challenges/two-strings/problem

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

# twoStrings has the following parameter(s):

# s1, s2: two strings to analyze .
# Input Format

# The first line contains a single integer , the number of test cases.

# The following  pairs of lines are as follows:

# The first line contains string .
# The second line contains string .
# Constraints

#  and  consist of characters in the range ascii[a-z].
# Output Format

# For each pair of strings, return YES or NO.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO
# Explanation

# We have  pairs to check:

# , . The substrings  and  are common to both strings.
# , .  and  share no common substrings.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    # Assumptions
    # strings fit on a single machine
    # strings are only lowercase

    # Approach Complexity Tradeoffs Improvements
    # Count characters in each
    # Then if every character in s1 is not in s2 there are no common substrings
    # O(s1 + s2) to count characters then O(1) to check since the number
    # of characters in ascii(a-z) is constant no matter how long the strings

    # Maybe we could count one char from each and stop to check for overlap
    # every 25 characters or so? That would catch many common substrings
    # early.

    # Could we convert each to a set instead? That is O(s1 + s2),
    # then check if there is an intersection? Yes we can and super simple.
    # plus similar runtime

    # Edge cases
    # long strings
    # empty strings (not included per problem statement)

    if set(s1).intersection(set(s2)):
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
