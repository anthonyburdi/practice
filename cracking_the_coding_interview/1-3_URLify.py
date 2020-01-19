# 1-3_URLify.py

# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string. Note:
# If implementing in Java, please use a character array so that you can
# perform this operation in place.

# Example
# Input: 'Mr John Smith    ', 13
# Output: 'Mr%20John%20Smith'

# Assumptions
# string is short enough to be stored in memory

# Approach
# trim leading and trailing spaces
# convert string to character array since Python strings are immutable
# change spaces to '%20'
# convert back to string and return

# Complexity
# Time complexity O(N) since we convert the string to a character array
# and back (both O(N)) and then check each character for a space
# Space complexity O(N) since we create a character array and a second string
# to return

# Possible improvements
# I'm not certain there can be

def urlify(s: str) -> str:
    """Replace spaces with '%20' after trimming whitespace."""

    # trim trailing and leading whitespace & convert to character array:
    s = list(s.strip())

    s = [char if char is not " " else "%20" for char in s]

    return "".join(s)

import unittest

class TestUrlify(unittest.TestCase):

    def test_example_1(self):

        self.assertEqual(
            urlify('Mr John Smith    '),
            'Mr%20John%20Smith'
        )

    def test_example_2(self):

        self.assertEqual(
            urlify('  the quick brown fox jumped over the lazy dog      '),
            "the%20quick%20brown%20fox%20jumped%20over%20the%20lazy%20dog"
        )

if __name__ == '__main__':
    unittest.main()

