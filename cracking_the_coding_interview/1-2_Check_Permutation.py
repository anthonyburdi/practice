# 1-2_Check_Permutation.py

# 1.2 Check Permutation
# Given two strings, write a method to decide if one is a permutation of the
# other.

def check_permutation(string1: str, string2: str) -> bool:
    """Determine if strings are a permutation of each other."""

    # Assumptions, Approach, Time & Space Complexity & Possible Improvements:
    # Assumptions:
    # All characters are valid, including spaces.
    # If both strings are null then return True.
    # Case sensitive - e.g. 'Pam' is not permutation of 'map'

    # Approach:
    # 1. Create character counts of each string and compare
    # 2. Brute force check each character in string1 by checking
    # in string2, then popping off that character. First have to
    # create character arrays e.g. ["a", "b", "b"] since in Python
    # strings are immutable
    # 3. Sort both strings in place and check for differences
    # by iterating through both at the same time. This is not actually
    # in place in python since strings are immutable.

    # Time & Space Complexity:
    # Approach 1: O(N) time since we loop through each string
    # Where N is character count of string1 + string2
    # O(1) space complexity since we are creating a new hashmap
    # for each that contains only the possible characters.
    # E.g. if N is large, we still only have a finite # of chars
    # Approach 2: O(N^2) time since we loop through both lists for
    # each item in string1. N here is really the lengths of strings
    # e.g. O(m * n). Slightly shorter if we pop off characters as
    # we find them.
    # O(1) space, but we do need to create new character arrays in Python
    # so it is really O(N) space.
    # Approach 3: O(NlogN) since we have to sort the strings first
    # Once sorted then it is O(N) so total time is still O(NlogN).
    # Space: O(N) in Python since strings are immutable & we have to
    # create character arrays or new sorted strings. Otherwise O(1)
    # if they come as character arrays or in a different language.

    # Possible improvements:
    # Check lengths. If unequal, return False.

    # Implementation of approach 1:

    if not len(string1) == len(string2):
        return False

    string1_counts = {}
    string2_counts = {}

    for character in string1:
        string1_counts[character] = string1_counts.get(character, 0) + 1
    for character in string2:
        string2_counts[character] = string2_counts.get(character, 0) + 1

    return string1_counts == string2_counts

import unittest

class TestCheckPermutation(unittest.TestCase):

    def test_blank_strings(self):
        self.assertEqual(
            check_permutation("", ""),
            True
        )


    def test_short_permuted_strings(self):
        self.assertEqual(
            check_permutation("abc", "cba"),
            True
        )


    def test_long_permuted_strings(self):
        self.assertTrue(
            check_permutation(
                "iamlordvoldemort",
                "lordearmoldvomit"
            )
        )
        self.assertTrue(
            check_permutation(
                "abracadabra",
                "arbadacarba"
            )
        )


    def test_short_non_permuted_strings(self):
        self.assertFalse(
            check_permutation("abc", "abd")
        )
        self.assertFalse(
            check_permutation("a", "asdfasdfasdf")
        )
        self.assertFalse(
            check_permutation("", "fjaksdfui")
        )


    def test_long_non_permuted_strings(self):
        self.assertFalse(
            check_permutation(
                "asdfasldkjasdlfkjasdflkjasdflkj",
                "opqiweuropiwqeurqpwoieurqwopeir"
            )
        )

        self.assertFalse(
            check_permutation(
                "asdfasdfasdfasdfasdfasdfasdfasdf",
                "qwerqwerqwerqwerqwerqwer"
            )
        )


    def test_permuted_strings_with_spaces(self):
        # spaces count, hence extra in 'rid dle':
        self.assertTrue(
            check_permutation(
                "i am lord voldemort",
                "tom marvolo rid dle"
            )
        )


    def test_non_permuted_strings_with_spaces(self):
        self.assertFalse(
            check_permutation(
                "I am Lord Voldemort",
                "Tom Marvolo Riddle"
            )
        )
        self.assertFalse(
            check_permutation(
                "I am Lord Voldemort",
                "Lord Ear Mold Vomit"
            )
        )


    def test_permuted_strings_with_numbers(self):
        self.assertTrue(
            check_permutation(
                "hello123",
                "123hello"
            )
        )


    def test_non_permuted_strings_with_numbers(self):
        self.assertFalse(
            check_permutation(
                "hello123",
                "hi456hi7"
            )
        )


if __name__ == '__main__':
    unittest.main()
