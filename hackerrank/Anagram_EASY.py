# Anagram_EASY.py

# https://www.hackerrank.com/challenges/anagram/problem

# Two words are anagrams of one another if their letters can be rearranged to form the other word.

# In this challenge, you will be given a string. You must split it into two contiguous substrings, then determine the minimum number of characters to change to make the two substrings into anagrams of one another.

# For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

# Function Description

# Complete the anagram function in the editor below. It should return the minimum number of characters to change to make the words anagrams, or  if it's not possible.

# anagram has the following parameter(s):

# s: a string
# Input Format

# The first line will contain an integer, , the number of test cases.
# Each test case will contain a string  which will be concatenation of both the strings described above in the problem.
# The given string will contain only characters in the range ascii[a-z].

# Constraints


#  consists only of characters in the range ascii[a-z].
# Output Format

# For each test case, print an integer representing the minimum number of changes required to make an anagram. Print  if it is not possible.

# Sample Input

# 6
# aaabbb
# ab
# abc
# mnop
# xyyx
# xaxbbbxx
# Sample Output

# 3
# 1
# -1
# 2
# 0
# 1
# Explanation

# Test Case #01: We split  into two strings ='aaa' and ='bbb'. We have to replace all three characters from the first string with 'b' to make the strings anagrams.

# Test Case #02: You have to replace 'a' with 'b', which will generate "bb".

# Test Case #03: It is not possible for two strings of unequal length to be anagrams of one another.

# Test Case #04: We have to replace both the characters of first string ("mn") to make it an anagram of the other one.

# Test Case #05:  and  are already anagrams of one another.

# Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". You must replace 'a' from S1 with 'b' so that S1 = "xbxb".


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):

    # Assumptions:
    # s is ascii[a-z]
    # s not empty
    # s fits on a single computer

    # Approach:
    # Check if even length
    # split in two and count characters in each
    # return count of non-overlapping characters
    # O(n) time complexity where n is the length of s
    # O(n) space complexity where n is len(s)
    # could do in place but O(n^2) time complexity for O(1) space

    # Edge cases
    # s empty (but its not)

    if len(s) % 2 != 0:
        return -1

    first_half_counts = {}
    second_half_counts = {}

    mid = len(s) // 2

    for i, char in enumerate(s):
        if i < mid:
            # count first half
            first_half_counts[char] = first_half_counts.get(char, 0) + 1
        else:
            # count second half
            second_half_counts[char] = second_half_counts.get(char, 0) + 1

    # check non overlapping characters
    for char, count in first_half_counts.items():
        if first_half_counts[char] < second_half_counts.get(char, 0):
            first_half_counts[char] = 0
        else:
            first_half_counts[char] -= second_half_counts.get(char, 0)

    return sum(first_half_counts.values())

    # Manual test
    # xaxbbbxx
    # mid = 4
    # i = 0 char = x
    # first_half_counts = {"x": 2, "a": 1, "b": 1}
    # second_half_counts = {"x": 2, "b": 2}

    # char = "x"
    # first_half_counts = {"x": 0, "a": 1, "b": 1}
    # char = "a"
    # first_half_counts = {"x": 0, "a": 1, "b": 1}
    # char = "b"
    # first_half_counts = {"x": 0, "a": 1, "b": 0}
    # return sum([0,1,0]) = 1 (correct)

    # mnop
    # mid = 2
    # first_half_counts = {"m": 1, "n": 1}
    # return sum([1,1])


    # asdfjoieufoa
    # fdhlvosfpafhalll
    # mvdalvkiopaufl

    # I'm getting 3 6 5
    # Should be 3 5 5
    # fdhlvosf pafhalll

    # fdhlvosfpafhalll
    # fdhlvosf pafhalll
    # first_half_counts = {"f": 2, "d": 1, "h": 1, "l": 1, "v": 1, "o": 1, "s": 1}
    # "f"
    # first_half_counts = {"f": 1, "d": 1, "h": 1, "l": 1, "v": 1, "o": 1, "s": 1}
    # "d"
    # first_half_counts = {"f": 1, "d": 1, "h": 1, "l": 1, "v": 1, "o": 1, "s": 1}
    # "h"
    # first_half_counts = {"f": 1, "d": 1, "h": 0, "l": 1, "v": 1, "o": 1, "s": 1}
    # "l"
    # first_half_counts = {"f": 1, "d": 1, "h": 0, "l": 0, "v": 1, "o": 1, "s": 1}
    # "v"
    # first_half_counts = {"f": 1, "d": 1, "h": 0, "l": 0, "v": 1, "o": 1, "s": 1}
    # "o"
    # first_half_counts = {"f": 1, "d": 1, "h": 0, "l": 0, "v": 1, "o": 1, "s": 1}
    # "s"
    # first_half_counts = {"f": 1, "d": 1, "h": 0, "l": 0, "v": 1, "o": 1, "s": 1}
    # return sum([1,1,0,0,1,1,1]) = 5


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
