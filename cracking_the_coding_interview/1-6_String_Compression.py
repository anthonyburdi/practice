# 1-6_String_Compression.py

# 1.6 String Compression
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can
# assume the string has only uppercase and lowercase letters (a-z).

def string_compression(s: str) -> str:
    """Compress a string with character counts e.g. aabcccccaaa -> a2b1c5a3."""

    # Assumptions, Approach, Time & Space Complexity & Possible Improvements:

    # Assumptions:
    # s contains only uppercase and lowercase letters
    # empty string returns empty string

    # Approach:
    # 1. Loop through string checking if current character is equal to the
    # previous character and if so incrementing a counter
    # if not, append the previous character with count to an array
    # appending to an array is faster/space efficient in python rather than
    # appending to a string since strings are immutable.
    # afterwards we join all the array strings together
    # Then check the length and if the compressed string is smaller, return it
    # otherwise return the given string.

    # Time & Space Complexity:
    # Time complexity is O(N) since we have to check each character
    # Space complexity is O(N) since we have to create the compressed
    # string. Generally this will be smaller than O(N), but O(N) in the
    # worst case where each character is different.

    # Possible improvements:
    # Maybe we can use an ordered dict python object to make the character
    # counts and then use that to create the compressed string

    # Approach 1:

    if not s:
        return ""

    # start with first character of the string
    previous_character = s[0]
    previous_character_counter = 0
    compressed_string_array = []

    for character in s:
        if character == previous_character:
            previous_character_counter += 1
        else:
            compressed_string_array.append(
                "{}{}".format(
                    previous_character,
                    previous_character_counter
                )
            )
            previous_character = character
            previous_character_counter = 1

    # also get last character
    compressed_string_array.append(
        "{}{}".format(
            previous_character,
            previous_character_counter
        )
    )

    compressed_string = "".join(compressed_string_array)

    if len(compressed_string) < len(s):
        return compressed_string
    else:
        return s


import unittest

class TestStringCompression(unittest.TestCase):

    def test_problem_example(self):

        self.assertEqual(
            string_compression("aabcccccaaa"),
            "a2b1c5a3"
        )


    def test_other_strings(self):
        self.assertEqual(
            string_compression("xxxyyyzzzhhhhheeeeelllllooooo"),
            "x3y3z3h5e5l5o5"
        )


    def test_empty_string(self):
        self.assertEqual(
            string_compression(""),
            ""
        )


    def test_string_shorter_than_compressed(self):
        self.assertEqual(
            string_compression("asdfqwer"),
            "asdfqwer"
        )


if __name__ == '__main__':
    unittest.main()