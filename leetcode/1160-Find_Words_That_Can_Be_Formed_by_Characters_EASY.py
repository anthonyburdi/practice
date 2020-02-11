# 1160-Find_Words_That_Can_Be_Formed_by_Characters_EASY.py

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.



# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation:
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


# Note:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        # Assumptions
        # strings are all english lowercase characters
        # words is not null, each word is not null, chars is not null

        # Approach
        # using a hashmap create character counts for chars
        # loop through words and count chars for each
        # Once char count is  made for a word, check if each char exists
        # and there are enough in chars. If all exist, then add len(word)
        # to our running count.
        # Time: O(n * w) where n is num words and w is avg length of word
        # Space: O(1) since at most each hashmap will have 26 entries.

        # Edge cases
        # letter exists in char but not enough
        # more letters exist in char than needed
        # not enough letters exist in chars
        # (not really edge cases but we need to handle these, real edge
        # cases are taken care of in the note)

        def check_word(word: str, word_map: dict, chars_map: dict):
            """Check if a word can be made from chars in chars_map."""

            for char in word:
                if chars_map.get(char, 0) < word_map.get(char, 0):
                    return False
            return True


        # initialize sum
        sum_words = 0

        # create hashmap of chars
        chars_map = {}
        for char in chars:
            chars_map[char] = chars_map.get(char, 0) + 1

        # loop through words
        for word in words:
            word_map = {}
            # create hashmap of word
            for word_char in word:
                word_map[word_char] = word_map.get(word_char, 0) + 1

            # Check if word is "good" if so add len to sum_words
            if check_word(word, word_map, chars_map):
                sum_words += len(word)


        return sum_words





