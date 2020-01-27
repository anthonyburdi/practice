# Repeated_String_EASY.py

# https://www.hackerrank.com/challenges/repeated-string/problem

# Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

# Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

# For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

# Constraints

# For  of the test cases, .
# Output Format

# Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7
# Explanation 0
# The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

# Sample Input 1

# a
# 1000000000000
# Sample Output 1

# 1000000000000
# Explanation 1
# Because all of the first  letters of the infinite string are a, we print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    # Assumptions
    # We can't just loop through adding a new string to the back of the string
    # whenever we run out of characters bc this takes too much time and space.
    # Also strings are immutable in python (though could be a char array).
    # n can be as large as 10^12
    # s is not empty and s is a string
    # n can be less than len(s)
    # n is an integer
    # always look for "a"

    # Approach
    # A faster & more space efficient approach might be to divide the
    # len of s into n, and also get the remainder. Then we can count
    # the occurrences in s, and multiply by the number of times s
    # fits into n. Then add the count in the len of s given by the
    # remainder.
    # we have to consider if n is smaller than s, so to avoid
    # counting the a's in s twice we can skip that count if len(s)//n == 0

    # to count the a's in s we just iterate through and add if we hit an a
    # however given a limit, we can iterate through and stop either when we
    # hit the end of the string or our counter is reached.

    # Complexity
    # Time
    # O(N) where N is the length of s. The other operations are constant time.
    # we loop through N at most twice
    # Space
    # O(1) since we are just keeping a few pointers and division results

    # Potential improvements
    # we can maybe loop through s counting the a's and not stop at the index
    # but just hold that count and keep counting the full amount. That way
    # we don't have to do it twice.

    # Edge Cases
    # n < len(s)
    # n very large
    # s small
    # n small

    full_substrings = n // len(s)
    partial_substring_len = n % len(s)

    as_in_partial_substring = 0
    as_in_full_substring = 0

    for i, char in enumerate(s):
        if char == "a":
            if (i + 1) <= partial_substring_len:
                as_in_partial_substring += 1
            elif full_substrings == 0:
                break
            as_in_full_substring += 1

    tot_a = (full_substrings * as_in_full_substring) + as_in_partial_substring

    return tot_a





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
