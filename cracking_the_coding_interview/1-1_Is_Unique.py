# 1-1_Is_Unique.py

# 1.1 Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(string: str) -> bool:
    """Determine if a string has all unique characters."""

    # Approach, Time & Space Complexity & Possible Improvements:
    # Approach:
    # 1. Add each character count to a hashmap (char is key, count is value)
    # if the character already exists and you are incrementing to 2, return
    # False. Otherwise return true if this never occurs.
    # 2. Also we can add the character to a set and check for existence
    # before returning False (rather than a hashmap of counts)
    # Approach without additional data structures:
    # 3. Sort string, iterate through and if the next character is the same
    # as the previous then return False
    # 4. Create a variable for each character count (NO this is still
    # O(N) space)
    # Time & Space Complexity:
    # Initial approach is O(N) time & space to build the hashmap
    # Without addition adata structures is O(NlogN) time complexity for sorting
    # O(NlogN) and then iterating through O(N) but O(1) space... actually
    # in python strings are immutable so O(N) space since the sorted string
    # takes O(N) space
    # Possible Improvements:
    # Check for existence in set (approach 2)

    # Approach 1
    # char_counts = {}

    # for character in string:
    #     char_counts[character] = char_counts.get(character, 0) + 1
    #     if char_counts[character] > 1:
    #         return False

    # return True

    # Approach 2
    char_set = set()

    for character in string:
        if character in char_set:
            return False
        else:
            char_set.add(character)

    return True

    # Approach 3
    # sorted_string = sorted(string)
    # previous_character = ''

    # for character in sorted_string:
    #     if character == previous_character:
    #         return False
    #     else:
    #         previous_character = character

    # return True

import unittest

class TestIsUnique(unittest.TestCase):

    def test_unique_str(self):
        self.assertEqual(
            is_unique("abcd"),
            True
        )

    def test_non_unique_str(self):
        self.assertEqual(
            is_unique("abccdd"),
            False
        )

    def test_empty(self):
        self.assertEqual(
            is_unique(""),
            True
        )

    def test_long_unique(self):
        self.assertEqual(
            is_unique("asdfghjkl;'qwertyuiop[]zxcvbnm,./1234567890-="),
            True
        )

    def test_long_non_unique(self):
        self.assertEqual(
            is_unique("asdfghjkl;'qwertyuiopqwertyuipoiasdljkasoicndiuopasd"),
            False
        )

if __name__ == '__main__':
    unittest.main()