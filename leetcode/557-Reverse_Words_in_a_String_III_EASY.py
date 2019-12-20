# 557-Reverse_Words_in_a_String_III_EASY.py

# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will
# not be any extra space in the string.

class Solution:
    def reverseWords(self, s: str) -> str:

        # Approach:
        # Split sentence by spaces into a list
        # For each word in the list reverse the characters and add to new list
        # Do this in the same order
        # Then join up all the words by spaces using .join()
        # Time Complexity:
        # For each step O(N), so O(N) total
        # Space Complexity:
        # O(N) since we add a new list of all the characters and new string
        # with all of the items joined
        # Possible Improvements:
        # Maybe we can do this in place to help the space complexity
        # However Python strings are immutable so we'd have to change this
        # to a character array first anyway which takes O(N) extra space
        # if it wasn't python we could create a temporary string after each
        # space character and then reverse that and overwrite the word

        # words = s.split(" ")
        # reversed_words = []
        # for word in words:
        #     reversed_word = word[::-1]
        #     reversed_words.append(reversed_word)

        # return " ".join(reversed_words)

        # Or in a single line:
        return " ".join([word[::-1] for word in s.split(" ")])





import unittest

class TestReverseWords(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        input_string = "Let's take LeetCode contest"
        output_string = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(
            self.solution.reverseWords(input_string),
            output_string
        )

    def test_example_2(self):
        input_string = ""
        output_string = ""
        self.assertEqual(
            self.solution.reverseWords(input_string),
            output_string
        )

if __name__ == '__main__':
    unittest.main()