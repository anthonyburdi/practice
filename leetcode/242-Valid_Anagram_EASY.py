# 242-Valid_Anagram_EASY.py

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Count characters using hashmap and compare
        # Unicode characters should compare correctly in python3 (I hope!)

        s_counts = {}
        t_counts = {}

        for letter_s in s:
            s_counts[letter_s] = s_counts.get(letter_s, 0) + 1

        for letter_t in t:
            t_counts[letter_t] = t_counts.get(letter_t, 0) + 1

        # Compare and don't worry about uppercase / lowercase per the question
        return s_counts == t_counts


if __name__ == '__main__':
    solution = Solution()

    s = "anagram"
    t = "nagaram"

    print("Example 1 should be True:", solution.isAnagram(s, t))

    s = "rat"
    t = "car"

    print("Example 2 should be False:", solution.isAnagram(s, t))