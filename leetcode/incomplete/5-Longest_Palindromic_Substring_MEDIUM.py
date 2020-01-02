# 5-Longest_Palindromic_Substring_MEDIUM.py

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


# Assumptions, Approach, Time & Space Complexity & Possible Improvements:

# Assumptions:
# max len(s) = 1000, so we can do this in memory
# palindrome must include at least 2 characters - NO SEE BELOW
# assume we can return any of the longest palindromes seen if they are equal
# length (see example 1)
# After checking test cases on leetcode, palindrome can include a single
# character. E.g. Input: "a", output: "a"
# This also extends to longer strings, e.g. Input: "ac", output: "a"
# Palindromes are case senstitive

# Approach:
# Brute force we can check whether each substring is a palindrome
# by running a pointer in both directions and checking to see if the string
# is the same forwards and backwards. We can iterate through the given string
# and have a sub loop getting every length of string from the current position
# of the outer loop to the end of the string. Then when we find any palindrome
# we keep track of it and length if it is bigger than any we have seen before.
# eventually we return the string of the longest palindrome we've seen.
# e.g. "cbbd"
# first loop we check "cb" "cbb" "cbbd"
# second loop we check "bb" (add 2 as max_len) "bbd"
# third loop we check "bd"
# then we return max_len = 2
# we can do this with a sub-function that checks whether a string is a
# palindrome, which returns false if any discrepancy is found (without going
# through the full string if found early to speed up a bit).
# I can't think of a better algorithm right now. I don't think we can use
# tries bc we need order of the characters.
# We can definitely skip checking the rest of the string if we already have
# a palindrome longer than the rest of the string that we haven't checked yet.
# That will help speed things up a little.

# Complexity:
# The brute force is O(n^2) because we loop through every combination of
# string length. This may not be correct since each string is smaller
# the further we go. Actually it is worse since we have to check whether
# a given string is a palindrome by looping through it... O(n^3)
# Space complexity is O(1) since we are only carrying a few extra variables

# Possible improvements
# if there are any repeated characters, we can assume at least max_len = 2
# maybe we can skip checking some cases using this info?
# Would recursion help in this case?

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Find a largest palindrome substring in a string."""

        if len(s) < 2:
            return s

        longest_palindrome_substring = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                candidate = s[i:j+1]
                palindrome = self.checkPalindrome(candidate)
                if palindrome:
                    if len(candidate) > len(longest_palindrome_substring):
                        longest_palindrome_substring = candidate

        return longest_palindrome_substring


    def checkPalindrome(self, s: str) -> bool:
        """Check whether an input string is a palindrome."""

        # See assumptions, smaller strings are considered palindromes
        # if len(s) < 2:
        #     return False

        forward = 0
        reverse = len(s) - 1

        while forward < reverse:
            if s[forward] is not s[reverse]:
                return False

            forward += 1
            reverse -= 1

        return True


import unittest

class TestCheckPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_palindromes_positive(self):
        self.assertTrue(self.solution.checkPalindrome("bab"))
        self.assertTrue(self.solution.checkPalindrome("babbab"))
        self.assertTrue(self.solution.checkPalindrome("ababa"))
        self.assertTrue(self.solution.checkPalindrome("asdfghjkllkjhgfdsa"))
        self.assertTrue(self.solution.checkPalindrome("babbabbabbab"))
        self.assertTrue(self.solution.checkPalindrome("!@#$%^&*())(*&^%$#@!"))


    def test_palindromes_negative(self):
        self.assertFalse(self.solution.checkPalindrome("baba"))
        self.assertFalse(self.solution.checkPalindrome("bababababa"))
        self.assertFalse(self.solution.checkPalindrome("ababababab"))
        self.assertFalse(self.solution.checkPalindrome("asdfghjkllkjhasdf"))
        self.assertFalse(self.solution.checkPalindrome("bbbbbbbbbaaaaaaaa"))
        self.assertFalse(self.solution.checkPalindrome("!@#$%^&*()"))


    def test_palindromes_edge_cases(self):
        self.assertTrue(self.solution.checkPalindrome(""))
        self.assertTrue(self.solution.checkPalindrome("a"))
        self.assertTrue(self.solution.checkPalindrome("!"))
        self.assertTrue(self.solution.checkPalindrome("aa"))
        self.assertTrue(self.solution.checkPalindrome("!!"))


class TestLongestPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.longestPalindrome("babad"),
            "bab"
        )


    def test_example_2(self):
        self.assertEqual(
            self.solution.longestPalindrome("cbbd"),
            "bb"
        )


    def test_positive(self):
        self.assertEqual(
            self.solution.longestPalindrome("bab"),
            "bab"
        )
        self.assertEqual(
            self.solution.longestPalindrome("baab"),
            "baab"
        )
        self.assertEqual(
            self.solution.longestPalindrome("bbbaaabbbasdfghjk"),
            "bbbaaabbb"
        )
        self.assertEqual(
            self.solution.longestPalindrome("!@#$%%$#@!&*(&)(*&(*&*("),
            "!@#$%%$#@!"
        )
        self.assertEqual(
            self.solution.longestPalindrome("54614asdfasdf123454321asdfad"),
            "123454321"
        )

    def test_negative(self):
        self.assertEqual(
            self.solution.longestPalindrome("asdfkljhasdhjaklsdhjfklajhdsf"),
            "a"
        )
        self.assertEqual(
            self.solution.longestPalindrome("123456127321351364324325345"),
            "1"
        )
        self.assertEqual(
            self.solution.longestPalindrome("&^*&(%^*(%)^*&%()&@#$(#@&$)(#"),
            "&"
        )


    def test_edge_cases(self):
        self.assertEqual(
            self.solution.longestPalindrome(""),
            ""
        )
        self.assertEqual(
            self.solution.longestPalindrome("1"),
            "1"
        )
        self.assertEqual(
            self.solution.longestPalindrome("a"),
            "a"
        )
        self.assertEqual(
            self.solution.longestPalindrome("ac"),
            "a"
        )
        self.assertEqual(
            self.solution.longestPalindrome("11"),
            "11"
        )
        self.assertEqual(
            self.solution.longestPalindrome("bb"),
            "bb"
        )


if __name__ == '__main__':
    unittest.main()





