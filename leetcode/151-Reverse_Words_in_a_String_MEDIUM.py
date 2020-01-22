# 151-Reverse_Words_in_a_String_MEDIUM.py

# https://leetcode.com/problems/reverse-words-in-a-string/

# Given an input string, reverse the string word by word.



# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.


# Follow up:

# For C programmers, try to solve it in-place in O(1) extra space.


class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse words in the given string."""

        # DISCUSSION -----------------------------------------------------------

        # Assumptions
        # string fits on a single machine (or api to string is the same if on
        # multiple machines)
        # OK to use a new array to hold the words, then join together
        # Since strings are immutable in python
        # We could also first make the string a character array but that uses
        # the same amount of space O(n) for char array, O(n) for reversed
        # words array, O(n) for output string.
        # Assume None input gives '' output

        # Approach
        # First isolate words.
        # Then create new string from reversed words list.
        # Isolate words by adding to a temporary character array when the
        # characters are not a space " ". When we hit a space, add that char
        # array as a string to the words list. Continue until we hit the next
        # character then start again.

        # Complexity:
        # Time: O(N) since we have to iterate through all the characters
        # then put them all back together into a new string
        # Space: O(N) since we have O(N) words list, O(N) reversed words array
        # and O(N) output string. We also have a temp char array O(N).

        # Potential improvements:
        # make the string a char array (see assumptions)
        # do this in-place on char array
        # One potential solution is by reversing the whole char array then
        # going back to re-reverse each word, and strip out extra spaces

        # Edge cases:
        # null string
        # all spaces
        # single space
        # all numeric
        # word then spaces
        # spaces then a word
        # single char
        # single word (no spaces)

        # IMPLEMENTATION -------------------------------------------------------

        return_string = ''
        words = []

        # Handle some edge cases:
        if s is None:
            return return_string

        # Isolate words

        # Strip leading and trailing spaces
        s = s.strip()
        # (Maybe I should also re-implement this?)

        char_array = list(s)

        word = []
        while char_array:
            char = char_array.pop(0)
            if word != [] and char == " ":
                words.append("".join(word))
                word = []
            elif word == [] and char == " ":
                continue
            else:
                word.append(char)

        if word != []:
            words.append("".join(word))

        return " ".join(reversed(words))


# Test by hand:
# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"

# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"

# Edge cases:
# null string
# all spaces
# single space
# all numeric
# word then spaces
# spaces then a word
# single char
# single word (no spaces)


import unittest

class TestReverseWords(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        i = "the sky is blue"
        o = "blue is sky the"
        self.assertEqual(self.solution.reverseWords(i), o)

    def test_example_2(self):
        i = "  hello world!  "
        o = "world! hello"
        self.assertEqual(self.solution.reverseWords(i), o)

    def test_example_3(self):
        i = "a good   example"
        o = "example good a"
        self.assertEqual(self.solution.reverseWords(i), o)

    def test_edge_cases(self):
        i = None
        o = ''
        self.assertEqual(self.solution.reverseWords(i), o)
        i = "             "
        o = ''
        self.assertEqual(self.solution.reverseWords(i), o)
        i = " "
        o = ''
        self.assertEqual(self.solution.reverseWords(i), o)
        i = " "
        o = ''
        self.assertEqual(self.solution.reverseWords(i), o)
        i = "   123    32   2233 3 3  "
        o = '3 3 2233 32 123'
        self.assertEqual(self.solution.reverseWords(i), o)
        i = "None   "
        o = 'None'
        self.assertEqual(self.solution.reverseWords(i), o)
        i = "     None"
        o = 'None'
        self.assertEqual(self.solution.reverseWords(i), o)
        i = "a"
        o = 'a'
        self.assertEqual(self.solution.reverseWords(i), o)
        i = "None"
        o = 'None'
        self.assertEqual(self.solution.reverseWords(i), o)


if __name__ == '__main__':
    unittest.main()









