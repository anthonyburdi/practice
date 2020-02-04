# Sherlock_and_the_Valid_String_MEDIUM.py

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

# For example, if , it is a valid string because frequencies are . So is  because we can remove one  and have  of each character in the remaining string. If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of .

# Function Description

# Complete the isValid function in the editor below. It should return either the string YES or the string NO.

# isValid has the following parameter(s):

# s: a string
# Input Format

# A single string .

# Constraints

# Each character
# Output Format

# Print YES if string  is valid, otherwise, print NO.

# Sample Input 0

# aabbcd
# Sample Output 0

# NO
# Explanation 0

# Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

# Sample Input 1

# aabbccddeefghi
# Sample Output 1

# NO
# Explanation 1

# Frequency counts for the letters are as follows:

# {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

# There are two ways to make the valid string:

# Remove  characters with a frequency of : .
# Remove  characters of frequency : .
# Neither of these is an option.

# Sample Input 2

# abcdefghhgfedecba
# Sample Output 2

# YES
# Explanation 2

# All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    # Assumptions
    # Characters are all lowercase a-z
    # String fits on a single machine

    # Approach, Complexity, Tradeoffs, Potential Improvements
    # 1. Two hash maps
    # the first hash map creates a character count (O(N) time O(1) space,
    # since the hashmap will be at most a constant 26 char long)
    # The second hash map counts the number of distinct character counts
    # We look at the second hash map. If there are more than two entries
    # then return NO
    # If there are exactly two entries, and both are greater than 1
    # then return NO
    # If there are exactly two entries, and at least one is == 1 then return
    # YES *** IF the one with 1 entry is within 1 of the other
    # otherwise return NO
    # if there is only one entry return YES
    # 2. Hmm I can't think of another better algorithm that doesn't use
    # another data structure but just iterates through the array. We could
    # use an array instead of a hash map but I don't see a big benefit.

    # Potential edge cases
    # empty string, single character, same character repeated


    # Create char count
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Create count count (num letters with given count)
    count_count = {}
    for char, count in char_count.items():
        count_count[count] = count_count.get(count, 0) + 1


    # print("string:", s)
    # print("char_count:", char_count)
    # print("count_count:", count_count)

    # Evaluate count count
    if len(count_count) == 1:
        return "YES"
    if len(count_count) > 2:
        return "NO"

    if len(count_count) == 2:
        # num of times we count a given char
        first_count = list(count_count.keys())[0]
        second_count = list(count_count.keys())[1]

        # num of chars for which we find that count
        first_count_count = count_count[list(count_count.keys())[0]]
        second_count_count = count_count[list(count_count.keys())[1]]

        # {char_count: num_chars_with_same_count}


         # See notebook for cases:

        if (
            (first_count == 1 and first_count_count == 1) or
            (second_count == 1 and second_count_count == 1)
        ):
            return "YES"

        elif (
            (first_count_count == 1 and (first_count - second_count == 1)) or
            (second_count_count == 1 and (second_count - first_count == 1))
        ):
            return "YES"

        else:
            return "NO"



import unittest

class TestIsValid(unittest.TestCase):

    def test_examples(self):

        self.assertEqual("NO", isValid("aaaabbcc"))

        s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"

        self.assertEqual("YES", isValid(s))

        self.assertEqual("NO", isValid("aabbcd"))

        self.assertEqual("NO", isValid("aaaaabc"))

        self.assertEqual("YES", isValid("abcdefghhgfedecba"))



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = isValid(s)

    # fptr.write(result + '\n')

    # fptr.close()

    # print("Should be NO:", isValid("aaaabbcc"))

    # s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"

    # print(len(s))

    # print("Should be YES:", isValid(s))

    # print("Should be NO:", isValid("aabbcd"))

    # print("Should be NO:", isValid("aaaaabc"))

    # print("Should be YES:", isValid("abcdefghhgfedecba"))


    unittest.main()










