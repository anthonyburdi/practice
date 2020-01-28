# Strings_Making_Anagrams.py

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

# Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

# For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.

# Function Description

# Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

# makeAnagram has the following parameter(s):

# a: a string
# b: a string
# Input Format

# The first line contains a single string, .
# The second line contains a single string, .

# Constraints

# The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
# Output Format

# Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

# Sample Input

# cde
# abc
# Sample Output

# 4
# Explanation

# We delete the following characters from our two strings to turn them into anagrams of each other:

# Remove d and e from cde to get c.
# Remove a and b from abc to get c.
# We must delete  characters to make both strings anagrams, so we print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    # Assumptions
    # Lowercase a-z
    # All are captured in the constraints

    # Approach, Complexity, Tradeoffs
    # create a hash map count of the letter frequency
    # iterate through the first hash map of a, checking at each point
    # for the item in the hash map of b. If it exists, add the abs value
    # of the difference to the num deletions
    # if it does not exist in b then add the freq in a to deletions
    # Then loop through the freq map of b and if an item is not in a then
    # add it's freq to deletions (since we already checked the intersection)
    # Time Complexity O(a + b) to make the hash maps
    # O(a) to check for a in b and O(b) for checking in a since checking
    # for existence in a hashmap is constant

    # Potential Improvements
    # I can't think of any

    # Edge Cases
    # len of a and b is 1 element

    def character_frequency_map(s: str) -> dict:
        """Return a dictionary of character: frequency in the given string."""
        frequency_map = {}
        for char in s:
            frequency_map[char] = frequency_map.get(char, 0) + 1
        return frequency_map


    # initialize
    deletions = 0
    # hash map count of a
    freq_a = character_frequency_map(a)
    # hash map count of b
    freq_b = character_frequency_map(b)
    # check for a in b
    for char, freq in freq_a.items():
        if char in freq_b:
            deletions += abs(freq - freq_b[char])
        else:
            deletions += freq

    # check for b in a
    for char, freq in freq_b.items():
        if char not in freq_a:
            deletions += freq_b[char]
    # return
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()























