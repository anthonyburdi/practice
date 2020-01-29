# Hash_Tables_Ransom_Note.py

# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is .

# Function Description

# Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .

# checkMagazine has the following parameters:

# magazine: an array of strings, each a word in the magazine
# note: an array of strings, each a word in the ransom note
# Input Format

# The first line contains two space-separated integers,  and , the numbers of words in the  and the ..
# The second line contains  space-separated strings, each .
# The third line contains  space-separated strings, each .

# Constraints

# .
# Each word consists of English alphabetic letters (i.e.,  to  and  to ).
# Output Format

# Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.

# Sample Input 0

# 6 4
# give me one grand today night
# give one grand today
# Sample Output 0

# Yes
# Sample Input 1

# 6 5
# two times three is not four
# two times two is four
# Sample Output 1

# No
# Explanation 1

# 'two' only occurs once in the magazine.

# Sample Input 2

# 7 4
# ive got a lovely bunch of coconuts
# ive got some coconuts
# Sample Output 2

# No
# Explanation 2

# Harold's magazine is missing the word .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    # Assumptions
    # Case sensitive
    # Words can be duplicated in note and magazine, must find all
    # All fits on a single machine

    # Approach, Complexity, Tradeoffs
    # 1. Brute force search through magazine for each word in note Time: O(M*N)
    # space O(1)
    # 2. Convert magazine to freq hashmap for quick existence lookups. Then
    # iterate through note and check for each word in magazine using hash map
    # if we find it, decrement freq or remove entry. If not return False.
    # O(M) to create hashmap of magazine O(N) to check for existence
    # Overall time complexity O(M + N). Space Complexity: O(M) for hashset
    # Tradeoff here is space for time.
    # I am forgetting the string comparisons. These are O(s) where
    # s is the lengths of the two strings (if equal). Python does some
    # optimization here caching object identifiers and then checking the len
    # before doing a char by char compare.
    # Actually no, this doesn't happen. Since we create a hash map, when
    # checking for existence we just make a hash of the item to be checked
    # and then locate that hash so it is still O(1)
    # I could be wrong on this!

    # Potential Improvements
    # Sorting to make searching easier would lead to worse performance
    # I can't think of any

    # Edge Cases
    # M or N is small
    # Convert magazine  to frequency hashmap
    magazine_freq = {}
    for word in magazine:
        magazine_freq[word] = magazine_freq.get(word, 0) + 1

    # Iterate through note and check each word for existence in magazine_freq
    # If exists, decrement magazine_freq count. If not, print “No”
    for word in note:
        if word in magazine_freq:
            if magazine_freq[word] ==  1:
                magazine_freq.pop(word)
            else:
                magazine_freq[word] -= 1
        else:
            print("No")
            return

    # if all good, print “Yes”
    print("Yes")
    return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
