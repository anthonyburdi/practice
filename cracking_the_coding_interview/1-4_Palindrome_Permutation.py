# 1-4_Palindrome_Permutation.py

# Given a string, write a function to check if it is a permutation of a
# palindrome.

# Example
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc)

# Assumptions:
# Ignore casing and non letter characters

# Approach:
# count characters
# all characters should have even counts except one can be odd (middle char)
# use a hash map for this (python dictionary)

# Time and space complexity:
# O(N) since we count each character
# O(1) space since we just keep a constant size dict with 26 letter keys

def palindrome_permutation(s: str) -> bool:
    """Check if string is a permutation of a palindrome."""

    # remove all non alpha characters then change to all lowercase
    s = s.replace(" ", "")
    s = ''.join([i for i in s if i.isalpha()])
    s = s.lower()

    char_counts = {}

    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    num_odd_counts = 0

    for key, value in char_counts.items():

        if not value % 2 == 0:
            num_odd_counts += 1
            if num_odd_counts > 1:
                return False

    return True



import unittest

class TestPalindromePermutation(unittest.TestCase):

    def test_example_1(self):
        s = "Tact Coa"
        self.assertTrue(palindrome_permutation(s))


    def test_false_example(self):
        s = "President Obama!"
        self.assertFalse(palindrome_permutation(s))


    def test_true_example(self):
        s = "Dammit, I’m Mad"
        self.assertTrue(palindrome_permutation(s))


if __name__ == '__main__':
    unittest.main()